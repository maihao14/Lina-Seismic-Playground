import numpy as np
def setstart(npts,itp,its):
    leftParrival = np.random.randint(0,min(1000,itp))
    startpoint = itp-leftParrival
    return startpoint,leftParrival

def labeldata(st,size = 9000):
    validmatrix = True
    for tr in st:
        if tr.stats.sampling_rate<1.0:
            st.remove(tr)
    # only use 3 channels data
    if len(st)>3:
        st = st[0:3]
        channels = 3
    else:
        channels = len(st)
    # non valid data exit
    if channels == 0:
        return [0,False,0,0,0]

    samplerate = st[0].stats.sampling_rate
    itp = 60*samplerate
    its =st[0].stats.npts-st[0].stats.sampling_rate*90

    if abs(its-itp)<size:
        st.resample(samplerate)
        if st[0].stats.npts<size:
            st.resample(60.0)
    else:
        return [0,False,0,0,0]


    # P S arrival exceed datasize (9000) points range exit
    samplerate = st[0].stats.sampling_rate
    itp = int(60*samplerate)
    its = int(st[0].stats.npts-st[0].stats.sampling_rate*90)
    if abs(its-itp)>size:
        return [0,False,0,0,0]
    # set a startpoint to crop data
    startpoint,itp = setstart(st[0].stats.npts,itp,its)
    if startpoint+size>st[0].stats.npts:
        startpoint = 0
        itp = int(60*samplerate)
    its = its - startpoint

    matrix=np.empty((size,1))
    for i in st:
        trace = i.data
        if (len(trace)>size)and(startpoint+size<i.stats.npts)and (startpoint>=0):
            matrix = np.c_[matrix,trace[int(startpoint):int(startpoint+size)]]
        else:
            return[0,False,0,0,0]

    matrix = matrix[:,1:]

    if np.size(matrix,1)==1:
        channels = st[0].stats.sac.kcmpnm
        matrix = np.c_[matrix,np.zeros((size,1))]
        matrix = np.c_[matrix,np.zeros((size,1))]
        return [matrix,validmatrix,itp,its,channels]
    if np.size(matrix,1)==2:
        channels = st[0].stats.sac.kcmpnm+'_'+st[1].stats.sac.kcmpnm
        matrix = np.c_[matrix,np.zeros((size,1))]
        return [matrix,validmatrix,itp,its,channels]
    if np.size(matrix,1)==3:
        channels = st[0].stats.sac.kcmpnm+'_'+st[1].stats.sac.kcmpnm+'_'\
        +st[2].stats.sac.kcmpnm
        return [matrix,validmatrix,itp,its,channels]
    return [matrix,validmatrix,itp,its,channels]

def NameTraces(file):
    str = ''
    n = -1;
    for i in file:
        n = n+1
        if not i == '_':
            str = str+i
        else:
            break
    prefixname = str[:-4]
    suffixname = file[n:-4]
    str = str[:-4]+'*'+file[n:]

    return [str,prefixname,suffixname]
def Produce(FilePath= './NA2008/',FileOut = './Label2008/'):
    import os
    from obspy import read
    fname=[]
    channels = []
    itpgroup=[]
    itsgroup=[]
    mags = []
    nets = []

    files= os.listdir(FilePath) #得到文件夹下的所有文件名称
    for file in files[:10]: #遍历文件夹
        [str,prefixname,suffixname] = NameTraces(file)
        filename = FilePath+str
        print(filename)
        st = read(filename)
        [data,validmatrix,itp,its,chs] = labeldata(st,9000)
        itp = int(itp)
        its = int(its)
        if validmatrix:
            npzfile = prefixname+suffixname+'.npz'
            if not npzfile in fname:
                fname.append(npzfile)
                channels.append(chs)
                itpgroup.append(itp)
                itsgroup.append(its)
                mags.append(st[0].stats.sac.mag)
                nets.append(st[0].stats.sac.knetwk)
                var = {'data':data,'itp':itp,'its':its,'channels':chs}
                np.savez(FileOut+npzfile, **var)
    return fname,itpgroup,itsgroup,channels,nets,mags

def save2csv(fname,itpgroup,itsgroup,channels,nets,mags,csvfile='NA2008.csv',csvstats='NA2008Stats.csv'):
    import csv
    a = { 'fname':fname,'itp':itpgroup,'its':itsgroup,'channels':channels}
    with open(csvfile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["fname", "itp", "its","channels"])
        for i in range(len(fname)):
            writer.writerow([a['fname'][i], a['itp'][i], a['its'][i], a['channels'][i]])
    b = { 'fname':fname, 'itp':itpgroup,'its':itsgroup,'channels':channels,'network':nets,'magnitude':mags}
    with open(csvstats, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["fname", "itp", "its","channels","network","magnitude"])
        for i in range(len(fname)):
            writer.writerow([b['fname'][i], b['itp'][i],b['its'][i],b['channels'][i],b['network'][i],b['magnitude'][i]])
