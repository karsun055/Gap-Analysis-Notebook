'''

Program Name = io_5MtsBaseForAnalysisSorted

Created on Jun 10, 2018

@author: karsu
'''
import pyodbc
import datetime
import db_utils as dbu
import os

def get5MtsBaseForAnalysisSortedColumnsDetails(conn):
    return dbu.getTableColumnsDetails(conn, '5MtsBaseForAnalysisSorted')



def get_all_5MtsBaseForAnalysisSorted_recs(conn):
    recs = dbu.get_all_recs(conn, '5MtsBaseForAnalysisSorted')
    return recs

if __name__ == '__main__': 
    db_file = r'''StooqDataAnalysis.accdb'''  #raw string, escape sequences are ignored
    db_file = os.path.abspath(db_file)
    dbConnData = dbu.createDBConnection(db_file)
    conn = dbu.createDBConnection(db_file)   
     
