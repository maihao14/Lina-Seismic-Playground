from obspy import read

def get_stream():
    st = read('http://examples.obspy.org/RJOB_061005_072159.ehz.new')
    return st
###
