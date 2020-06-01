#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:51:43 2020

@author: hao
"""

def plot_matrix_wave(st,itp,its):
    import matplotlib.pyplot as plt
    import numpy as np
    j=0
    plt.figure(figsize=(8, 4.5))
    #plt.title(tr.stats.sac.knetwk+tr.stats.sac.kcmpnm+' '+str(tr.stats.sac.mag)+' Earthquake',verticalalignment='top')
    for j in np.arange(3):
        plt.subplot(3,1,j+1)
        plt.plot(st[:,j], 'k')
#        plt.ylabel(tr.stats.sac.kcmpnm)
        plt.axvline(itp,label="1",color='blue',linestyle="--")
        plt.axvline(its,label="2",color='red',linestyle="--")
#    title = tr.stats.sac.knetwk+tr.stats.sac.kcmpnm+' '+str(tr.stats.sac.mag)+' Earthquake'+'\n'
    plt.suptitle('Label Data')
    plt.xlabel('Time [s]')
    plt.show()