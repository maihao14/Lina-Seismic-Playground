# How to Label Seismic Data for Deep Learning

> This is an example of how to make label datasets for deep learning.

In this demo, I'll cover how to organize the raw data into the same dimensions for making training sets. How to convert a SAC file to a Python npz file, and record waveform information simultaneously.

![image](https://github.com/maihao14/Lina-Seismic-Playground/blob/master/LabelData/IntroIMG.png)

## Getting Started 使用指南

Install Package: [/LabelSAC2NPZ/](https://github.com/maihao14/Lina-Seismic-Playground/tree/master/LabelData/LabelSAC2NPZ).

```
python setup.py install
```

'''


### Prerequisites 项目使用条件

[Obspy](https://github.com/obspy/obspy)

```
pip install obspy
```

### Installation 安装

[Download](https://github.com/maihao14/Lina-Seismic-Playground/tree/master/LabelData) LabelData/ this folder into your local address. Then you can setup above Package:
[/LabelSAC2NPZ/](https://github.com/maihao14/Lina-Seismic-Playground/tree/master/LabelData/LabelSAC2NPZ).

OS X & Linux:

```sh
cd ./where_you_download_this_folder/LabelData/
python setup.py install
```

Windows:

```sh
cd ./where_you_download_this_folder/LabelData/
python setup.py install
```

### Usage example 使用示例

### Data Quick View
Read a SAC sample in NA2008 folder. Check trace information in .sac file.

```
from obspy import read
import matplotlib.pyplot as plt
import os
import numpy as np
from obspy import read
path = './NA2008/'
file = '*_2008-04-15T05_49_17.307_2008-04-15T05_52_34.529.sac'
file1 = '*_2008-04-15T06_56_51.087_2008-04-15T07_02_13.673.sac'
file2 = '*_2008-04-30T03_05_15.335_2008-04-30T03_10_44.451.sac'
file3 = '*_2008-12-06T04_19_02.862_2008-12-06T04_22_35.229.sac'
st = read(path+file, debug_headers=True)
#st = read(path1+file3, debug_headers=True)

#take first compponent as example:
print('Network: ', st[0].stats.sac.knetwk)
print('Channel: ',st[0].stats.sac.kcmpnm)
print('Event Magnitude: ',st[0].stats.sac.mag )
print('Samplerate: ',st[0].stats.sampling_rate)
print('Number of sample points: ',st[0].stats.npts)
```
Output:

Network:  CI <br>
Channel:  BHZ<br>
Event Magnitude:  3.2<br>
Samplerate:  40.0<br>
Number of sample points:  7889<br>

### Plot a simple graph of the current traces
```
from LabelSAC2NPZ.plot_raw_wave import plot_raw_wave
plot_raw_wave(st)
```
Output:<br>
![Image](https://github.com/maihao14/Lina-Seismic-Playground/blob/master/LabelData/RawIMG.png)

## Deployment 部署方法
### Create same size labels
We set default trace size: 9000 points <br>
Accepted channels: >= 1.0Hz sampling rate <br>
From folder: /NA2008/ read SAC files <br>
Convert to 9000 points channels samples<br>
Save to folder: /Label2008/<br>
```
from LabelSAC2NPZ import createlabel
LabelSAC2NPZ.Produce('./NA2008/','./Label2008/')
```
Output:
![image](https://github.com/maihao14/Lina-Seismic-Playground/blob/master/LabelData/SampleIMG.png) <br>

Output folder [Label2008](https://github.com/maihao14/Lina-Seismic-Playground/tree/master/LabelData/Label2008) contains over 50,000 standard waveform samplings with P/S arrival time. <br>

### Save events information into CSV files:
#### [NA2008.csv](https://github.com/maihao14/Lina-Seismic-Playground/blob/master/LabelData/NA2008.csv)

|  fname   | itp  | its | channels |
|  ----  | ----  |  ---- |  ---- |
|  II.PFO.00_2009-03-20T.npz|  676| 4438| BHZ_LHZ|
|  IM.NV01._2009-01-19T.npz| 751|7756 |SHZ |

#### [NA2008Stats.csv](https://github.com/maihao14/Lina-Seismic-Playground/blob/master/LabelData/NA2008Stats.csv)

|  fname   | itp  | its | channels |network|magnitude|
|  ----  | ----  |  ---- |  ---- |---- |  ---- |
|  II.PFO.00_2009-03-20T.npz |676|4438 | BHZ_LHZ|II|3.2|
| IM.NV01._2009-01-19T.npz |751 |7756 | SHZ|IM|1.7|

## Contributing 贡献指南

Please read [CONTRIBUTING.md](#) for details on our code of conduct, and the process for submitting pull requests to us.

清阅读 [CONTRIBUTING.md](#) 了解如何向这个项目贡献代码

## Release History 版本历史

* 0.2.1
    * CHANGE: Update docs
* 0.2.0
    * CHANGE: Remove `README.md`
* 0.1.0
    * Work in progress

## Authors 关于作者

* **WangYan** - *Initial work* - [WangYan](https://wangyan.org)

查看更多关于这个项目的贡献者，请阅读 [contributors](#)

## License 授权协议

这个项目 MIT 协议， 请点击 [LICENSE.md](LICENSE.md) 了解更多细节。
