# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 10:21:46 2019

@author: XPIEMART
"""
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import numpy
from scipy import stats


#read buffer data and buffergraphs' positions
#bufferdata = pd.read_csv('data.csv')
#position = pd.read_csv('GraphPosition.csv')
#read flow data
#frd = pd.read_csv('flow_relation.csv')

def time_format(bufferdata):
    #convert time string to time
    #delete the day bit of tha time stamp since it is not relevant
    for i in range(len(bufferdata['Time Stamp'])):
       var = bufferdata['Time Stamp'][i].split(":")
       date_time_obj = var[1]+":"+var[2]+":"+var[3]
       result_time = datetime.datetime.strptime(date_time_obj,'%H:%M:%S.%f')
       bufferdata['Time Stamp'][i] = result_time.time()



def buffer_report_plot(bufferdata,position,zero_buffer,highp_buffer,lowp_buffer,graphs_output):
    ####define grid's size####
    #total number of objects to plot
    objectstab = bufferdata.iloc[:,2:len(bufferdata.columns)]
    #add 1 as it doesn't start at 0 - i.e. array
    gridcolvalue = position['column'].max() + 1
    gridrowvalue = position['row'].max() + 1
    #define time value
    time = bufferdata['X_AXIS']

    fig, axes = plt.subplots(nrows=gridrowvalue, ncols=gridcolvalue, figsize=(50,20))
    a=0
    for i in objectstab:
        #highlight buffer color if reached 0
        if i in zero_buffer:
            #to change backgroundcolour
            #axes[position.iloc[a]['row'],position.iloc[a]['column']].set_facecolor('xkcd:green')
            axes[position.iloc[a]['row'],position.iloc[a]['column']].spines['bottom'].set_color('xkcd:green')
            axes[position.iloc[a]['row'],position.iloc[a]['column']].spines['top'].set_color('xkcd:green')
            axes[position.iloc[a]['row'],position.iloc[a]['column']].spines['right'].set_color('xkcd:green')
            axes[position.iloc[a]['row'],position.iloc[a]['column']].spines['left'].set_color('xkcd:green')
        if i in highp_buffer:
            axes[position.iloc[a]['row'],position.iloc[a]['column']].spines['bottom'].set_color('xkcd:aquamarine')
            axes[position.iloc[a]['row'],position.iloc[a]['column']].spines['top'].set_color('xkcd:aquamarine')
            axes[position.iloc[a]['row'],position.iloc[a]['column']].spines['right'].set_color('xkcd:aquamarine')
            axes[position.iloc[a]['row'],position.iloc[a]['column']].spines['left'].set_color('xkcd:aquamarine')
        if i in lowp_buffer:
            axes[position.iloc[a]['row'],position.iloc[a]['column']].spines['bottom'].set_color('xkcd:tomato')
            axes[position.iloc[a]['row'],position.iloc[a]['column']].spines['top'].set_color('xkcd:tomato')
            axes[position.iloc[a]['row'],position.iloc[a]['column']].spines['right'].set_color('xkcd:tomato')
            axes[position.iloc[a]['row'],position.iloc[a]['column']].spines['left'].set_color('xkcd:tomato')

        axes[position.iloc[a]['row'],position.iloc[a]['column']].plot(time, bufferdata[i],color='black',linewidth=0.2)
        axes[position.iloc[a]['row'],position.iloc[a]['column']].set_title(i)
        axes[position.iloc[a]['row'],position.iloc[a]['column']].set(
                xlabel='shift',
                ylabel='buffer contents')

        if bufferdata[i].min() == 0:
            ymin = bufferdata[i].min()
        else:
            ymin = bufferdata[i].min() - 1
        #sets the axes at origin
        axes[position.iloc[a]['row'],position.iloc[a]['column']].set_ylim([ymin,bufferdata[i].max()+1])
       # axes[position.iloc[a]['row'],position.iloc[a]['column']].set_xlim([time.min(),len(bufferdata.index)])
        axes[position.iloc[a]['row'],position.iloc[a]['column']].set_xlim([time.min(),time.max()])

        a += 1

    #remove blank graphs
    for x in range(gridrowvalue):
        for y in range(gridcolvalue):
            if not axes[x,y].has_data():
                axes[x,y].remove()

    plt.tight_layout()
    plt.savefig(graphs_output)

    #x = datetime.datetime.now()
    #plt.savefig('foo_'+ x.strftime("%c")+'.pdf')
    #plt.savefig('foo_'+str(x.minute) + '.pdf')
