#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:26:19 2020

@author: hao
"""

# Waveform
#Create a simple graph of the current traces.
def plot_raw_wave(st):
    import matplotlib.pyplot as plt
    import numpy as np
    j=0
    plt.figure(figsize=(8, 4.5))
    #plt.title(tr.stats.sac.knetwk+tr.stats.sac.kcmpnm+' '+str(tr.stats.sac.mag)+' Earthquake',verticalalignment='top')
    for tr in st:
        j=j+1
        trace = tr.data
        t = np.linspace(0, tr.stats.npts / tr.stats.sampling_rate, num=tr.stats.npts )
        plt.subplot(len(st),1,j)
        plt.plot(t, trace, 'k')
        plt.ylabel(tr.stats.sac.kcmpnm)
        itp = 60 # p arrival
        its =tr.stats.npts / tr.stats.sampling_rate - 90 # s arrival
        plt.axvline(its,label="1",color='blue',linestyle="--")
        plt.axvline(itp,label="2",color='red',linestyle="--")
    title = tr.stats.sac.knetwk+tr.stats.sac.kcmpnm+' '+str(tr.stats.sac.mag)+' Earthquake'+'\n'
    plt.suptitle(title+str(tr.stats.starttime))
    plt.xlabel('Time [s]')
    plt.show()
