'''
Program Name = io_StooqCrossTabTable

Created on Jun 10, 2018

@author: karsu
'''

import pyodbc
import datetime
import makeAccessDBConnection
import db_utils as dbu
import os


#===============================================================================

def insert_recs(conn, outrec):
    
    c = conn.cursor()
    

    sql = """ insert into StooqCrossTabTable (Ticker, \
    CurDate, \
    PDayCloseTime, \
    PDayOpen, \
    PDayLow, \
    PDayHigh, \
    PDayClose, \
    PDayVolume, \
    CDayOpenTime, \
    CDayOpenOpen, \
    CDayOpenLow, \
    CDayOpenHigh, \
    CDayOpenClose, \
    CDayOpenVolume, \
    CDay1000AMTime, \
    CDay1000AMOpen, \
    CDay1000AMLow, \
    CDay1000AMHigh, \
    CDay1000AMClose, \
    CDay1000AMVolume, \
    CDay1030AMTime, \
    CDay1030AMOpen, \
    CDay1030AMLow, \
    CDay1030AMHigh, \
    CDay1030AMClose, \
    CDay1030AMVolume, \
    CDay1100AMTime, \
    CDay1100AMOpen, \
    CDay1100AMLow, \
    CDay1100AMHigh, \
    CDay1100AMClose, \
    CDay1100AMVolume, \
    CDay0400PMTime, \
    CDay0400PMOpen, \
    CDay0400PMLow, \
    CDay0400PMHigh, \
    CDay0400PMClose, \
    CDay0400PMVolume    
    ) values \
    (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """
    
    c.execute(sql, \
    outrec['Ticker'], \
    outrec['CurDate'], \
    outrec['PDayCloseTime'], \
    outrec['PDayOpen'], \
    outrec['PDayLow'], \
    outrec['PDayHigh'], \
    outrec['PDayClose'], \
    outrec['PDayVolume'], \
    outrec['CDayOpenTime'], \
    outrec['CDayOpenOpen'], \
    outrec['CDayOpenLow'], \
    outrec['CDayOpenHigh'], \
    outrec['CDayOpenClose'], \
    outrec['CDayOpenVolume'], \
    outrec['CDay1000AMTime'], \
    outrec['CDay1000AMOpen'], \
    outrec['CDay1000AMLow'], \
    outrec['CDay1000AMHigh'], \
    outrec['CDay1000AMClose'], \
    outrec['CDay1000AMVolume'], \
    outrec['CDay1030AMTime'], \
    outrec['CDay1030AMOpen'], \
    outrec['CDay1030AMLow'], \
    outrec['CDay1030AMHigh'], \
    outrec['CDay1030AMClose'], \
    outrec['CDay1030AMVolume'], \
    outrec['CDay1100AMTime'], \
    outrec['CDay1100AMOpen'], \
    outrec['CDay1100AMLow'], \
    outrec['CDay1100AMHigh'], \
    outrec['CDay1100AMClose'], \
    outrec['CDay1100AMVolume'], \
    outrec['CDay0400PMTime'], \
    outrec['CDay0400PMOpen'], \
    outrec['CDay0400PMLow'], \
    outrec['CDay0400PMHigh'], \
    outrec['CDay0400PMClose'], \
    outrec['CDay0400PMVolume'])
    
    conn.commit()
    
def getCrossTabColumnsDetails(conn):
    return dbu.getTableColumnsDetails(conn, 'StooqCrossTabTable')

def get_all_StooqCrossTabTable_recs(conn):
    recs = dbu.get_all_recs(conn, 'StooqCrossTabTable')
    return recs


def getFieldType(field_names,column_details):
    for rec in column_details:
        if (rec[0] == field_names):
            return rec[1]
    
def get_selective_recs(conn,field_names,operands, values):

    column_details = getCrossTabColumnsDetails(conn)
    critera_list = list(zip(field_names, operands, values))
    print(critera_list)
    

    c = conn.cursor()
    sql = """ SELECT * FROM StooqCrossTabTable WHERE """
    criteria_no = 0
    
    if (len(field_names) > 1):
        multiple_criteria = True
        
    for criteria in critera_list:
        criteria_no = criteria_no + 1
        
        sql = sql + "( [" + criteria[0] +"] " + criteria[1] + " "
        field_type = getFieldType(criteria[0], column_details)
    
#    print(field_type)
# result = zip(numberList, strList)
    
        if (field_type ==  str):
            sql = sql + "'" + criteria[2] + "' )"

        if (field_type ==  datetime.datetime):
            sql = sql + criteria[2] + " )"
                                  
        if (multiple_criteria and criteria_no < len(field_names)):
            sql = sql + " AND "
        
    print(sql)
    c.execute(sql)

    columns = [column[0] for column in c.description]
    
    recs = []
    for row in c.fetchall():
        recs.append(dict(zip(columns, row)))
    
    return recs

if __name__ == '__main__': 
    db_file = r'''StooqDataAnalysis.accdb'''  #raw string, escape sequences are ignored
    db_file = os.path.abspath(db_file)
    dbConnData = dbu.createDBConnection(db_file)
    conn = dbu.createDBConnection(db_file)   
    
# Selective records ===========================================================
#     field_names = ['Ticker', 'CurDate']
#     operands = ['=', '=']
# #    values = ['A','datetime.date(year=2018, month=3, day=15)']
#     values = ['A','#3/16/2018#']
#     
#     in_recs = get_selective_recs(conn, field_names, operands, values)
#     
#     for rec in in_recs:
#         for k, v in rec.items():
#              print(k, v)
#         break
#===============================================================================
    
# datetime.time(hour=4, minute=0, second=0)    
#in_recs = get_all_recs(conn)

#===============================================================================
# for rec in in_recs:
#     for k, v in rec.items():
#         print(k, v)
#     break
#===============================================================================
    

