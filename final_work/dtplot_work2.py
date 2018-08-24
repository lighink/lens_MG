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

def plot(TDGRatMG_work2_1,TDMG_work2_1,TDGRatMG_work2_2,TDMG_work2_2,TDGRatMG_work2_3,TDMG_work2_3,TDGRatMG_work2_4,TDMG_work2_4):
    
    mpl.rcParams['text.usetex'] = 'True'
    rc('text.latex', preamble = r'\usepackage{mathrsfs}')
    mpl.rcParams['axes.linewidth'] = 1.1
    mpl.rcParams['font.size'] = 15.0
    mpl.rcParams['xtick.major.pad'] = 6
    mpl.rcParams['xtick.minor.pad'] = 6
    mpl.rcParams['ytick.major.pad'] = 6
    mpl.rcParams['ytick.minor.pad'] = 6

    
    
    
    plt.xlim(0,0.7)
    plt.ylim(0,15)
    #plt.axhspan(0,(TDGR[1,1]-TDGRc[1,1])/TDGR[1,1], color='green', alpha=0.2)
    plt.axhline(1.166,ls='dashed', color='#01A9DB',linewidth=2)
    plt.axhspan(0,1.166,color='#01A9DB', alpha=0.5)
    plt.axhline(8,ls='dashed', color='#BDBDBD',linewidth=2)
    plt.axhspan(0,8,color='#BDBDBD', alpha=0.5)
   # plt.axvline(0.3445,ls='dotted',color='red', linewidth=0.5)
   # plt.axvline(0.3295,ls='dotted',color='blue', linewidth=0.5)
   # plt.axvline(0.5345,ls='dotted',color='#084B8A', linewidth=0.5)
   # plt.axvline(0.412,ls='dotted',color='#FF8000', linewidth=0.5)
    #plt.plot(TDGR[:,0],(TDGR[:,1]-TDGRc[:,1])/TDGR[:,1],ls='dashed', color='green',linewidth=1.5,label="$2\sigma$ variation of $H_0$ given by Planck")
    
    plt.plot(TDGRatMG_work2_1[0:701,0],100.0*(TDMG_work2_1[0:701,1]-TDGRatMG_work2_1[0:701,1])/TDGRatMG_work2_1[0:701,1],color='red',linewidth=2,label=r'$r_{01}=10~\texttt{kpc},\frac{\delta\Sigma}{\Sigma}=12\%$')
   
    plt.plot(TDGRatMG_work2_1[701,0],100.0*(TDMG_work2_1[701,1]-TDGRatMG_work2_1[701,1])/TDGRatMG_work2_1[701,1],'r*')
    
    plt.plot(TDGRatMG_work2_2[0:652,0],100.0*(TDMG_work2_2[0:652,1]-TDGRatMG_work2_2[0:652,1])/TDGRatMG_work2_2[0:652,1],color='blue',linewidth=2.5,label=r'$r_{01}=20~\texttt{kpc},\frac{\delta\Sigma}{\Sigma}=8\%$')
    
    plt.plot(TDGRatMG_work2_2[652,0],100.0*(TDMG_work2_2[652,1]-TDGRatMG_work2_2[652,1])/TDGRatMG_work2_2[652,1],'b*')
    
    plt.plot(TDGRatMG_work2_3[0:1069,0],100.0*(TDMG_work2_3[0:1069,1]-TDGRatMG_work2_3[0:1069,1])/TDGRatMG_work2_3[0:1069,1],color='#084B8A',linewidth=3,label=r'$r_{01}=10~\texttt{kpc},\frac{\delta\Sigma}{\Sigma}=70\%$')
    
    plt.plot(TDGRatMG_work2_3[1069,0],100.0*(TDMG_work2_3[1069,1]-TDGRatMG_work2_3[1069,1])/TDGRatMG_work2_3[1069,1],'*',c='#084B8A')
    
    plt.plot(TDGRatMG_work2_4[0:817,0],100.0*(TDMG_work2_4[0:817,1]-TDGRatMG_work2_4[0:817,1])/TDGRatMG_work2_4[0:817,1],color='#FF8000',linewidth=3.5,label=r'$r_{01}=20~\texttt{kpc},\frac{\delta\Sigma}{\Sigma}=58\%$')
    
    plt.plot(TDGRatMG_work2_4[817,0],100.0*(TDMG_work2_4[817,1]-TDGRatMG_work2_4[817,1])/TDGRatMG_work2_4[817,1],'*',c='#FF8000')
    
    plt.legend(loc = 'upper right', fontsize = 10, frameon = True, numpoints = 1, handletextpad = 0.5, ncol = 1)
    
    
    
    
    
    plt.xlabel('$y[\\theta_E]$')
    plt.ylabel(r'$[(\Delta t_{MG}-\Delta t_{GR})/\Delta t_{GR}]\%$')
    plt.savefig("delta_t_plot_2.pdf", format = 'pdf', bbox_inches = 'tight')
    
if __name__=="__main__":    
    
    
    TDGRatMG_work2_1=loadtxt("./TDGRatMG_SIS_work2_1.txt")
    TDMG_work2_1=loadtxt("./TDMG_SIS_work2_1.txt")
    TDGRatMG_work2_2=loadtxt("./TDGRatMG_SIS_work2_2.txt")
    TDMG_work2_2=loadtxt("./TDMG_SIS_work2_2.txt")
    TDGRatMG_work2_3=loadtxt("./TDGRatMG_SIS_work2_3.txt")
    TDMG_work2_3=loadtxt("./TDMG_SIS_work2_3.txt")
    TDGRatMG_work2_4=loadtxt("./TDGRatMG_SIS_work2_4.txt")
    TDMG_work2_4=loadtxt("./TDMG_SIS_work2_4.txt")



    
    plot(TDGRatMG_work2_1,TDMG_work2_1,TDGRatMG_work2_2,TDMG_work2_2,TDGRatMG_work2_3,TDMG_work2_3,TDGRatMG_work2_4,TDMG_work2_4)    
