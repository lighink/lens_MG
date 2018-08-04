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

def plot(TDGR_work1,TDMG_work1,TDGRatMG_work2_1,TDMG_work2_1,TDGRatMG_work2_2,TDMG_work2_2):
    
    mpl.rcParams['text.usetex'] = 'True'
    rc('text.latex', preamble = r'\usepackage{mathrsfs}')
    mpl.rcParams['axes.linewidth'] = 1.1
    mpl.rcParams['font.size'] = 15.0
    mpl.rcParams['xtick.major.pad'] = 6
    mpl.rcParams['xtick.minor.pad'] = 6
    mpl.rcParams['ytick.major.pad'] = 6
    mpl.rcParams['ytick.minor.pad'] = 6

    
    
    
    plt.xlim(0,1)
    plt.ylim(0,8.0)
    #plt.axhspan(0,(TDGR[1,1]-TDGRc[1,1])/TDGR[1,1], color='green', alpha=0.2)
    plt.axhline(1.166,ls='dashed', color='#01A9DB',linewidth=2)
    plt.axhspan(0,1.166,color='#01A9DB', alpha=0.5)
    plt.axhline(5.13,ls='dashed', color='#BDBDBD',linewidth=2)
    plt.axhspan(0,5.13,color='#BDBDBD', alpha=0.5)
    #plt.plot(TDGR[:,0],(TDGR[:,1]-TDGRc[:,1])/TDGR[:,1],ls='dashed', color='green',linewidth=1.5,label="$2\sigma$ variation of $H_0$ given by Planck")
    
    plt.plot(TDGR_work1[:,0],100.0*(TDGR_work1[:,1]-TDMG_work1[:,1])/TDGR_work1[:,1],color='red', linewidth=2,label=r'Method 1: $r_1=0.01,\frac{\delta\Sigma}{\Sigma}=10\%$')
    plt.plot(TDGRatMG_work2_1[:,0],100.0*(TDMG_work2_1[:,1]-TDGRatMG_work2_1[:,1])/TDGRatMG_work2_1[:,1],color='#084B8A',linewidth=2.5,label=r'Method 2: $r_1=0.01,\frac{\delta\Sigma}{\Sigma}=4.5\%$')
    
    plt.plot(TDGRatMG_work2_2[:,0],100.0*(TDMG_work2_2[:,1]-TDGRatMG_work2_2[:,1])/TDGRatMG_work2_2[:,1],color='#FF8000',linewidth=3,label=r'Method 2: $r_1=0.021,\frac{\delta\Sigma}{\Sigma}=10\%$')
    
    
    plt.legend(loc = 'upper right', fontsize = 10, frameon = True, numpoints = 1, handletextpad = 0.5, ncol = 1)
    
    
    
    
    
    plt.xlabel('$y[\\theta_E]$')
    plt.ylabel(r'$[(\Delta \tau_{MG}-\Delta \tau_{GR})/\Delta \tau_{GR}]\%$')
    plt.savefig("delta_t_plot.pdf", format = 'pdf', bbox_inches = 'tight')
    
if __name__=="__main__":    
    
    
    TDGR_work1=loadtxt("./TDGR_SIS_work1.txt")
    TDMG_work1=loadtxt("./TDMG_SIS_work1.txt")
    TDGRatMG_work2_1=loadtxt("./TDGRatMG_SIS_work2_1.txt")
    TDMG_work2_1=loadtxt("./TDMG_SIS_work2_1.txt")
    TDGRatMG_work2_2=loadtxt("./TDGRatMG_SIS_work2_2.txt")
    TDMG_work2_2=loadtxt("./TDMG_SIS_work2_2.txt")

    plot(TDGR_work1,TDMG_work1,TDGRatMG_work2_1,TDMG_work2_1,TDGRatMG_work2_2,TDMG_work2_2)    
