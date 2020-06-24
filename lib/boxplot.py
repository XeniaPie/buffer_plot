# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:48:56 2020

@author: XPIEMART
"""

import matplotlib.pyplot as plt
import numpy as np

def plot(bufferdata,master_table,boxplot_output):
    buffer_qties = []
    for i in range(len(bufferdata.columns)-2):
        buffer_qties.append(bufferdata.iloc[:,2+i])

    # Multiple box plots on one Axes
    fig, ax = plt.subplots(figsize=(80,50))
    fig.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

    #Editing colors, and shapes
    '''
    bp = ax.boxplot(buffer_qties, notch=0, sym='.', vert=1, whis=1.5)
    plt.setp(bp['boxes'], color='grey')
    plt.setp(bp['whiskers'], color='grey')
    plt.setp(bp['fliers'], color='red', marker='+')
    '''

    # Add a horizontal grid to the plot, but make it very light in color
    # so we can use it for reading data values but not be distracting
    ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)
    # Hide these grid behind plot objects
    ax.set_axisbelow(True)
    #set the titles, fontsizes and axes limits
    ax.set_title('Comparison of Buffer Levels Statistics',fontsize=70)
    ax.set_xlabel('Buffers',fontsize=50)
    ax.set_ylabel('Buffer Values Distribution',fontsize=50)
    ax.tick_params(axis='both', which='major', labelsize=30)
    ax.set_ylim(-1,30)
    ax.set_xticklabels(master_table['Name'],rotation=45, fontsize=35)
    ax.boxplot(buffer_qties,showfliers=False,showmeans=True)
    #save and show graph
    plt.savefig(boxplot_output)

if __name__ == "__main__":
    pass
