'''
Program  Name - createStooqCrossTabTable

Created on Jun 10, 2018
@author: karsu
'''
#import makeAccessDBConnection
import os, sys
import pyodbc
import io_5MtsBaseForAnalysisSorted as base5
import io_StooqCrossTabTable as scrt
import datetime
import logging
import db_utils as dbu

logging.basicConfig(filename='test.log', level=logging.DEBUG, format = '%(module)s:%(levelname)s:%(lineno)d:%(message)s')
    
def move_prev_close_data_to_outrec():
    outrec['PDayCloseTime'] = prevclosedata['CDay0400PMTime']
    outrec['PDayOpen'] = prevclosedata['CDay0400PMOpen']
    outrec['PDayLow'] = prevclosedata['CDay0400PMLow']
    outrec['PDayHigh'] = prevclosedata['CDay0400PMHigh']
    outrec['PDayClose'] = prevclosedata['CDay0400PMClose']
    outrec['PDayVolume'] = prevclosedata['CDay0400PMVolume']

def setPrevDayData():
    prevclosedata['Ticker'] =  inrec['Ticker']
    prevclosedata['CurDate'] = inrec['CurDate']
    prevclosedata['CDay0400PMTime'] = inrec['CurTime']
    prevclosedata['CDay0400PMOpen'] = inrec['Open']
    prevclosedata['CDay0400PMLow'] = inrec['Low']
    prevclosedata['CDay0400PMHigh'] = inrec['High']
    prevclosedata['CDay0400PMClose'] = inrec['Close']
    prevclosedata['CDay0400PMVolume'] = inrec['Volume']

def setnine35amData():
    outrec['Ticker'] =  inrec['Ticker']
    outrec['CurDate'] = inrec['CurDate']
    outrec['CDayOpenTime'] = inrec['CurTime']
    outrec['CDayOpenOpen'] = inrec['Open']
    outrec['CDayOpenLow'] = inrec['Low']
    outrec['CDayOpenHigh'] = inrec['High']
    outrec['CDayOpenClose'] = inrec['Close']
    outrec['CDayOpenVolume'] = inrec['Volume']

def settenamData():
    outrec['CDay1000AMTime'] = inrec['CurTime']
    outrec['CDay1000AMOpen'] = inrec['Open']
    outrec['CDay1000AMLow'] = inrec['Low']
    outrec['CDay1000AMHigh'] = inrec['High']
    outrec['CDay1000AMClose'] = inrec['Close']
    outrec['CDay1000AMVolume'] = inrec['Volume']

def setten30amData():
    outrec['CDay1030AMTime'] = inrec['CurTime']
    outrec['CDay1030AMOpen'] = inrec['Open']
    outrec['CDay1030AMLow'] = inrec['Low']
    outrec['CDay1030AMHigh'] = inrec['High']
    outrec['CDay1030AMClose'] = inrec['Close']
    outrec['CDay1030AMVolume'] = inrec['Volume']

def setelevenamData():
    outrec['CDay1100AMTime'] = inrec['CurTime']
    outrec['CDay1100AMOpen'] = inrec['Open']
    outrec['CDay1100AMLow'] = inrec['Low']
    outrec['CDay1100AMHigh'] = inrec['High']
    outrec['CDay1100AMClose'] = inrec['Close']
    outrec['CDay1100AMVolume'] = inrec['Volume']

def setfourpmData():
    outrec['CDay0400PMTime'] = inrec['CurTime']
    outrec['CDay0400PMOpen'] = inrec['Open']
    outrec['CDay0400PMLow'] = inrec['Low']
    outrec['CDay0400PMHigh'] = inrec['High']
    outrec['CDay0400PMClose'] = inrec['Close']
    outrec['CDay0400PMVolume'] = inrec['Volume']
    

#===============================================================================

def initprevclosedata():
#    logging.debug('prev close data initialized')
    prevclosedata = {
        'Ticker': None,
        'CurDate':None,
        'CDay0400PMTime':None,
        'CDay0400PMOpen':None,
        'CDay0400PMLow':None,
        'CDay0400PMHigh':None,
        'CDay0400PMClose':None,
        'CDay0400PMVolume':None    
    }
    return prevclosedata

def initinrecdata():
#    logging.debug('in-rec initialized')
    inrec = {}
    for column in baseColumns:
        inrec[column[0]] = None
    return inrec

def initoutrecdata():
    outrec = {}
    for column in outrecColumns:
        outrec[column[0]] = None
    return outrec
#===============================================================================

db_file = 'StooqDataAnalysis.accdb'  #raw string, escape sequences are ignored
db_file = os.path.abspath(db_file)
    
conn = dbu.createDBConnection(db_file)

c = conn.cursor()

begdate = datetime.date(2018, 3, 14)

fourpmtime = datetime.time(16, 0, 0)

nine35amtime = datetime.time(9, 35, 0)

tenamtime = datetime.time(10, 0, 0)

ten30amtime = datetime.time(10, 30, 0)

elevenamtime = datetime.time(11, 0, 0)


baseColumns = base5.get5MtsBaseForAnalysisSortedColumnsDetails(conn)
outrecColumns = scrt.getCrossTabColumnsDetails(conn)

inrecsall = base5.get_all_5MtsBaseForAnalysisSorted_recs(conn)
#logging.debug('total in-recs = ' + str(len(inrecsall)))

if (len(inrecsall)) <= 0 :
    print('no records in 5MtsBaseForAnalysisSorted table')
    sys.exit()

firstday = True
firstTickerrec = True

pticker = inrecsall[0]['Ticker']
pdate = inrecsall[0]['CurDate'].date()

inrec = {}
prevclosedata = {}
outrec = {}

inrec = initinrecdata()
outrec = initoutrecdata()
prevclosedata = initprevclosedata()

#print(prevclosedata)
#print(prevclosedata['CDay0400PMTime'])

for rec in inrecsall:
    inrec = initinrecdata()

    inrec['Ticker'] = rec['Ticker']
    inrec['CurDate'] = rec['CurDate']
    inrec['CurTime'] = rec['CurTime']
    inrec['Open'] = rec['Open']
    inrec['Low'] = rec['Low']
    inrec['High'] = rec['High']
    inrec['Close'] = rec['Close']
    inrec['Volume'] = rec['Volume']

    cticker = inrec['Ticker']
    cdate = inrec['CurDate'].date()
    ctime = inrec['CurTime'].time()
    
#    logging.debug('Prev Ticker,date = {} - {} - {}'.format(pticker,pdate))
#    logging.debug('curr Ticker,date,time = {} - {} - {}'.format(cticker,cdate,ctime))
#    print('previous : ' + pticker + ' ' + str(pdate))
#    print('Current : ' + cticker + ' ' + str(cdate) + ' ' + str(ctime))
           
    if (pticker != cticker):
#        write_to_db(outrec)
        scrt.insert_recs(conn, outrec)        
        pticker = inrec['Ticker']
        pdate = inrec['CurDate'].date()
#        ptime = inrec['CurTime'].time()
        firstday = True
        outrec = initoutrecdata()
    elif (pdate != cdate):
        if (outrec['PDayCloseTime']):
#            write_to_db(outrec)
            scrt.insert_recs(conn, outrec)        
            pdate = inrec['CurDate'].date()
            outrec = initoutrecdata()
        else:
            pdate = inrec['CurDate'].date()            
        
    if (firstTickerrec):
        if (cdate < begdate):
            continue
        else:
            pticker = inrec['Ticker']
            pdate = inrec['CurDate'].date()
#            ptime = inrec['CurTime'].time()
            firstTickerrec = False
                
    if (firstday):
        if (ctime != fourpmtime) :
            continue
        else:
            setPrevDayData()
            firstday = False
            continue

    if  (ctime == nine35amtime) :
        move_prev_close_data_to_outrec()
        prevclosedata = initprevclosedata()
        setnine35amData()
#        print(outrec)
        continue
   
    if  (ctime == tenamtime) :
        settenamData()
        continue
   
    if  (ctime == ten30amtime) :
        setten30amData()
        continue
   
    if  (ctime == elevenamtime) :
        setelevenamData()
        continue
   
    if  (ctime == fourpmtime) :
        setfourpmData()
        setPrevDayData()
        continue
   
print('Program Completed')  