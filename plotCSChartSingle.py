'''
Program Name - plotCSChartSingle.py

Created on Jun 14, 2018

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

def plot_chart(times, opens, highs, lows, closes, file_name):
    
    trace = plotlygo.Candlestick(x=times,
                       open=opens,
                       high=highs,
                       low=lows,
                       close=closes)
    
    layout = plotlygo.Layout(
        xaxis = dict(
            rangeslider = dict(
                visible = False
            )
        )
    )
    data = [trace]
    fig = plotlygo.Figure(data=data,layout=layout)
    plotly.image.save_as(fig, filename= file_name +'.png')