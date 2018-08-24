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

def plot(TDGR_work1,TDMG_work1_1,TDMG_work1_2,TDMG_work1_3):
    
    mpl.rcParams['text.usetex'] = 'True'
    rc('text.latex', preamble = r'\usepackage{mathrsfs}')
    mpl.rcParams['axes.linewidth'] = 1.1
    mpl.rcParams['font.size'] = 15.0
    mpl.rcParams['xtick.major.pad'] = 6
    mpl.rcParams['xtick.minor.pad'] = 6
    mpl.rcParams['ytick.major.pad'] = 6
    mpl.rcParams['ytick.minor.pad'] = 6

    
    
    
    plt.xlim(0,1)
    plt.ylim(0,15.0)
    #plt.axhspan(0,(TDGR[1,1]-TDGRc[1,1])/TDGR[1,1], color='green', alpha=0.2)
    plt.axhline(5.13,ls='dashed', color='#BDBDBD',linewidth=2)
    plt.axhspan(0,5.13,color='#BDBDBD', alpha=0.5)
    #plt.plot(TDGR[:,0],(TDGR[:,1]-TDGRc[:,1])/TDGR[:,1],ls='dashed', color='green',linewidth=1.5,label="$2\sigma$ variation of $H_0$ given by Planck")
    
    plt.plot(TDGR_work1[:,0],100.0*(TDGR_work1[:,1]-TDMG_work1_1[:,1])/TDGR_work1[:,1],color='red', linewidth=2,label=r'$r_{01}=10~\texttt{kpc},\frac{\delta\Sigma}{\Sigma}=18\%$')
    
    plt.plot(TDGR_work1[:,0],100.0*(TDGR_work1[:,1]-TDMG_work1_2[:,1])/TDGR_work1[:,1],color='blue', linewidth=2.5,label=r'$r_{01}=20~\texttt{kpc},\frac{\delta\Sigma}{\Sigma}=50\%$')
    
    plt.plot(TDGR_work1[:,0],100.0*(TDGR_work1[:,1]-TDMG_work1_3[:,1])/TDGR_work1[:,1],color='purple', linewidth=3,label=r'$r_{01}=10~\texttt{kpc},\frac{\delta\Sigma}{\Sigma}=50\%$')
    
    plt.legend(loc = 'upper right', fontsize = 10, frameon = True, numpoints = 1, handletextpad = 0.5, ncol = 1)
    
    
    
    
    
    plt.xlabel('$y[\\theta_E]$')
    plt.ylabel(r'$[(\Delta t_{GR}-\Delta t_{MG})/\Delta t_{GR}]\%$')
    plt.savefig("delta_t_plot_1.pdf", format = 'pdf', bbox_inches = 'tight')
    
if __name__=="__main__":    
    
    
    TDGR_work1=loadtxt("./TDGR_SIS_work1.txt")
    TDMG_work1_1=loadtxt("./TDMG_SIS_work1_1.txt")
    TDMG_work1_2=loadtxt("./TDMG_SIS_work1_2.txt")
    TDMG_work1_3=loadtxt("./TDMG_SIS_work1_3.txt")


    plot(TDGR_work1,TDMG_work1_1,TDMG_work1_2,TDMG_work1_3)    
