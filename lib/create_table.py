# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:12:01 2020

@author: XPIEMART
"""
import pandas as pd


#prints first row of values: df1.iloc[0]
def gen_table(bufferdata):
    data = {'Name':[],'Buffer Levels':[],'Position':[],
            'Main':[],'Mean':[],'Median':[],'STD':[],
            'Skewness':[],'Variance':[], 'P0':[],'P25':[],
            'P50':[],'P75':[],'P100':[]}
    return pd.DataFrame(data)
if __name__ == "__main__":
    pass
