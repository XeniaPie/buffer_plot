# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:46:48 2020

@author: XPIEMART
"""

import pandas as pd
import numpy
from scipy import stats

#populate buffer names and values
def populate_values(bufferdata,master_table):
    #buffers object list
    buffers = list(bufferdata)
    del buffers[:2]
    #populate object buffers
    for x in range(len(buffers)):
        master_table.loc[x,'Name'] = buffers[x]
    #populate buffers values
    values_list = []
    for y in range(len(buffers)):
        foo_list = list(bufferdata.iloc[:,y+2])
        values_list.append(foo_list)

    for z in range(len(buffers)):
        master_table.loc[z,'Buffer Levels'] = str(values_list[z])

    return (master_table)

#populate plot position
def position(master_table,position):
    for i in range(len(position.index)):
        pos_list = []
        pos_list.append(position.iloc[i,1])
        pos_list.append(position.iloc[i,2])
        master_table.loc[i,'Position'] = str(pos_list)
    return (master_table)

#populate True/False for main line buffers
def buffer_main(master_table,frd):
    main_buffers = []
    flag = False
    for j in range(1,len(frd.columns)):
        flag = False
        for i in range(len(frd.index)):
            if frd.iat[i,j] == 1:
                for x in range(i,len(frd.index)):
                    if frd.iat[x,j] == 2:
                        flag = True
                        main_buffers.append(frd.columns[j])
        if flag == True:
            master_table.loc[j-1,'Main'] = True
        else:
            master_table.loc[j-1,'Main'] = False
    return (master_table)
#Statistics file - get all calculations done and populated to master table
def stats_table(master,bufferdata):

    '''
    for i in range(len(master.index)):
        #mean
        mean = numpy.mean(master.loc[i,'Buffer Levels'])
        master.loc[i,'Mean'] = mean
        #median
        median = numpy.median(master.loc[i,'Buffer Levels'])
        master.loc[i,'Median'] = median
        #Standard Deviation
        std = numpy.std(master.loc[i,'Buffer Levels'])
        master.loc[i,'STD'] = std
        #skewness
        skewness = stats.skew(master.loc[i,'Buffer Levels'])
        master.loc[i,'Skewness'] = skewness
        #variance
        variance = numpy.var(master.loc[i,'Buffer Levels'])
        master.loc[i,'Variance'] = variance

        for x in range(0,125,25):
            percentile = numpy.percentile(master.loc[i,'Buffer Levels'],x)
            master.loc[i,'P'+str(x)] = percentile
    '''
    for i in range(len(master.index)):
        #mean
        mean = numpy.mean(bufferdata.iloc[:,i+2])
        master.loc[i,'Mean'] = mean
        #median
        median = numpy.median(bufferdata.iloc[:,i+2])
        master.loc[i,'Median'] = median
        #Standard Deviation
        std = numpy.std(bufferdata.iloc[:,i+2])
        master.loc[i,'STD'] = std
        #skewness
        skewness = stats.skew(bufferdata.iloc[:,i+2])
        master.loc[i,'Skewness'] = skewness
        #variance
        variance = numpy.var(bufferdata.iloc[:,i+2])
        master.loc[i,'Variance'] = variance

        for x in range(0,125,25):
            percentile = numpy.percentile(bufferdata.iloc[:,i+2],x)
            master.loc[i,'P'+str(x)] = percentile

#first rule
def value_to_zero(bufferdata):
    # check if any buffer reaches 0cap
    buff_to_zero = []
    for j in range(2,len(bufferdata.columns)):
        for i in range(len(bufferdata.index)):
            #iat for index based item access
             value = bufferdata.iat[i,j]
             if value == 0:
                buff_to_zero.append(bufferdata.columns[j])

    #delete duplicate buffers
    buff_to_zero = list(dict.fromkeys(buff_to_zero))
    return buff_to_zero

#comparison between p50,p75,p100
#this shows whether a buffer is maintained at max capacity or not
def hihgp_comparison(master_table):
    highp_comp = []
    for i in range(len(master_table.index)):
        #iat for index based item access
         p50 = master_table.at[i,'P50']
         p75 = master_table.at[i,'P75']
         p100 = master_table.at[i,'P100']
         if p50 == p75 or p50 == p75 == p100 or p75 == p100:
            highp_comp.append(master_table.iat[i,0])

    #delete duplicate buffers
    highp_comp = list(dict.fromkeys(highp_comp))
    return highp_comp

def percentile_to_zero(master_table):
    lowp_comp = []
    for i in range(len(master_table.index)):
        #iat for index based item access
         p50 = master_table.at[i,'P50']
         p25 = master_table.at[i,'P25']
         if p50 == 0 or p25 == 0:
            lowp_comp.append(master_table.iat[i,0])

    #delete duplicate buffers
    lowp_comp = list(dict.fromkeys(lowp_comp))
    return lowp_comp

if __name__ == "__main__":
    pass
