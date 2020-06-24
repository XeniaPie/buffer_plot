# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:27:19 2020

@author: XPIEMART
"""
def parse_arguments():
    parser = argparse.ArgumentParser(description="run_plot")
    parser.add_argument('-d','--data',action = 'store', dest = 'bufferdata_location')
    parser.add_argument('-p','--graphpos',action = 'store', dest = 'position_location')
    parser.add_argument('-f','--flowrelation',action = 'store', dest = 'flowrelation_location')
    parser.add_argument('-g','--graphs_output',action = 'store', dest = 'graphs_output')
    parser.add_argument('-b','--boxplot_output',action = 'store', dest = 'boxplot_output')
    args= parser.parse_args()
    return args,parser

if __name__ == "__main__":
    import pandas as pd
    import lib.graph_generator as graph_gen
    import lib.calculations as calc
    import lib.create_table as table
    import lib.boxplot as boxplot
    import argparse

    args,parser = parse_arguments()

    if (args.bufferdata_location is not None) & \
        (args.position_location is not None) & \
        (args.flowrelation_location is not None):

        #read buffer data and buffergraphs' positions
        bufferdata = pd.read_csv(args.bufferdata_location)
        position = pd.read_csv(args.position_location)
        frd = pd.read_csv(args.flowrelation_location)
        #create master table
        master_table = table.gen_table(bufferdata)
        #populate names, buffer levels and positions
        calc.populate_values(bufferdata,master_table)
        calc.position(master_table,position)
        #populate main/subs
        calc.buffer_main(master_table,frd)
        #does all statistics calculations
        calc.stats_table(master_table,bufferdata)
        #formatting the time column
        graph_gen.time_format(bufferdata)
        #getting buffers that reach capacity 0
        zero_buffer = calc.value_to_zero(bufferdata)    #if P50=P75=P100 GREEN
        highp_buffer = calc.hihgp_comparison(master_table)    #if P25 or P50 = 0 RED
        lowp_buffer = calc.percentile_to_zero(master_table)
        #populate graphs and save
        graph_gen.buffer_report_plot(bufferdata,position,zero_buffer,highp_buffer,lowp_buffer,args.graphs_output)
        #generalte boxplot graph
        boxplot.plot(bufferdata,master_table,args.boxplot_output)
    else:
        parser.print_help()
