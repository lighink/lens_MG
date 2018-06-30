# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:12:15 2018

@author: lighink
"""

import matplotlib.pyplot as plt

from numpy import loadtxt

from matplotlib.ticker import ScalarFormatter, LogLocator
from matplotlib import rc
import matplotlib as mpl
import numpy as np

def plot(TDGR,TDGRc,TDMG1,TDMG2,TDMG3):
    
    mpl.rcParams['text.usetex'] = 'True'
    rc('text.latex', preamble = r'\usepackage{mathrsfs}')
    mpl.rcParams['axes.linewidth'] = 1.1
    mpl.rcParams['font.size'] = 15.0
    mpl.rcParams['xtick.major.pad'] = 6
    mpl.rcParams['xtick.minor.pad'] = 6
    mpl.rcParams['ytick.major.pad'] = 6
    mpl.rcParams['ytick.minor.pad'] = 6

    
    
    
    plt.xlim(0,1)
    plt.ylim(0,0.05)
    #plt.axhspan(0,(TDGR[1,1]-TDGRc[1,1])/TDGR[1,1], color='green', alpha=0.2)
    plt.axhline(0.012,ls='dashed', color='skyblue',linewidth=2)
    plt.axhspan(0,0.012,color='skyblue', alpha=0.5)
    plt.plot(TDGR[:,0],(TDGR[:,1]-TDGRc[:,1])/TDGR[:,1],ls='dashed', color='green',linewidth=1.5,label="$2\sigma$ variation of $H_0$ given by Planck")
    
    plt.plot(TDGR[:,0],(TDGR[:,1]-TDMG1[:,1])/TDGR[:,1],color='red', linewidth=2,label="MG: $r01=0.01,w01=0.0012$")
    plt.plot(TDGR[:,0],(TDGR[:,1]-TDMG2[:,1])/TDGR[:,1],color='blue',linewidth=2.5,label="MG: $r01=0.02,w01=0.0012$")
    plt.plot(TDGR[:,0],(TDGR[:,1]-TDMG3[:,1])/TDGR[:,1],color='purple',linewidth=3,label="MG: $r01=0.01,w01=0.0157$")
    
    
    
    plt.legend(loc = 'upper right', fontsize = 10, frameon = True, numpoints = 1, handletextpad = 0.5, ncol = 1)
    
    
    
    
    
    plt.xlabel('$y(\\theta_E)$')
    plt.ylabel("$(\Delta t-\Delta t_{GR})/\Delta t_{GR}$")
    plt.savefig("deltatplot.pdf", format = 'pdf', bbox_inches = 'tight')
    
if __name__=="__main__":    
    
    
    TDGR=loadtxt("./TDGR_SIS.txt")
    TDGRc=loadtxt("./TDGRc_SIS.txt")
    TDMG1=loadtxt("./TDMG_SIS_1.txt")
    TDMG2=loadtxt("./TDMG_SIS_2.txt")
    TDMG3=loadtxt("./TDMG_SIS_3.txt")
    
    plot(TDGR,TDGRc,TDMG1,TDMG2,TDMG3)    