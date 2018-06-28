# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt

from numpy import loadtxt

from matplotlib.ticker import ScalarFormatter, LogLocator
from matplotlib import rc
import matplotlib as mpl
import numpy as np

def plot(L,deltaphi):
    
    
    mpl.rcParams['text.usetex'] = 'True'
    rc('text.latex', preamble = r'\usepackage{mathrsfs}')
    mpl.rcParams['axes.linewidth'] = 1.1
    mpl.rcParams['font.size'] = 15.0
    mpl.rcParams['xtick.major.pad'] = 6
    mpl.rcParams['xtick.minor.pad'] = 6
    mpl.rcParams['ytick.major.pad'] = 6
    mpl.rcParams['ytick.minor.pad'] = 6
    
    
    
    plt.xlim(0,0.15)
    plt.ylim(-0.05,0.05)
    plt.plot(deltaphi,L,color='red',linewidth=2,label="$\Delta \hat{\Phi}(b=0.0068,L)$")
    
    plt.legend(loc = 'upper right', fontsize = 10, frameon = False, numpoints = 1, handletextpad = 0.5, ncol = 1)
    
    plt.xlabel('$\Delta \hat{\Phi}$')
    plt.ylabel("$L$")
    plt.savefig('deltaphiplot.pdf')
    
    
    
    
if __name__=="__main__":    
    
    
    (L,deltaphi)=loadtxt("./deltaphi.txt", usecols=(0,1), unpack='True')
    
    
    plot(L,deltaphi)