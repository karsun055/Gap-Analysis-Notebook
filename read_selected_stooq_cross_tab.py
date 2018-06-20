'''
Program Nmae - read_selected_stooq_cross_tab.py

Created on Jun 15, 2018

@author: karsu
'''
import os, sys
import pyodbc
import makeAccessDBConnection
import datetime
import logging
import io_5MtsBaseForAnalysisSorted as base5
import io_StooqCrossTabTable as sct
import db_utils as dbu
import plotly.plotly as plotly
import plotly.graph_objs as plotlygo
import plotCSChartSingle

def get_selected_cross_tab_rec(ticker, date):
    
#    print(ticker, date)
    year,month,date = date.split("-")
#    print(year, month, date)
    date = "#" + month + "/" + date + "/" + year + "#"
    db_file = r'''C:\TickData2018\StooqDataAnalysis.accdb'''  #raw string, escape sequences are ignored
    conn = dbu.createDBConnection(db_file)
    
    field_names = ['Ticker', 'CurDate']
    operands = ['=', '=']
    #    values = ['A','datetime.date(year=2018, month=3, day=15)']
    #values = ['A','#3/16/2018#']
    values = [ticker,date]
    
    in_recs = sct.get_selective_recs(conn, field_names, operands, values)
    
    for rec in in_recs:
 
        times = [datetime.time(hour=4, minute=0, second=0),
             datetime.time(hour=9, minute=35, second=0),
             datetime.time(hour=10, minute=0, second=0),
             datetime.time(hour=10, minute=30, second=0),
             datetime.time(hour=11, minute=0, second=0),
             datetime.time(hour=16, minute=0, second=0)]
         
        opens = [rec['PDayOpen'],
                 rec['CDayOpenOpen'],
                 rec['CDay1000AMOpen'],
                 rec['CDay1030AMOpen'],
                 rec['CDay1100AMOpen'],
                 rec['CDay0400PMOpen']
                 ]
        
        lows = [rec['PDayLow'],
                 rec['CDayOpenLow'],
                 rec['CDay1000AMLow'],
                 rec['CDay1030AMLow'],
                 rec['CDay1100AMLow'],
                 rec['CDay0400PMLow'],
                ]
    
        highs = [rec['PDayHigh'],
                 rec['CDayOpenHigh'],
                 rec['CDay1000AMHigh'],
                 rec['CDay1030AMHigh'],
                 rec['CDay1100AMHigh'],
                 rec['CDay0400PMHigh'],
                ]
                 
        closes = [rec['PDayClose'],
                 rec['CDayOpenClose'],
                 rec['CDay1000AMClose'],
                 rec['CDay1030AMClose'],
                 rec['CDay1100AMClose'],
                 rec['CDay0400PMClose'],
                ]
                             
        file_name = 'cs2'
        plotCSChartSingle.plot_chart(times, opens, highs, lows, closes, file_name)
    
#    print(len(in_recs))
    
if __name__ == '__main__':
    date = "2018-03-15" 
    get_selected_cross_tab_rec('A', date)
