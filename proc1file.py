'''
Created on Jun 4, 2018

@author: karsu
'''
#import os, sys
#import pyodbc
import csv
import db_utils as dbu

def getSingleFileData(filename, output):
 
    rawFile = filename
    removePath = rawFile.split("\\") [-1]
    ticker = removePath.split('.')[0]    # format - Date, Time, open, high, low, close, volume
    # print(data.read())
    
    temp_line = []
    total_result = []
    single_result = []
    lineNo = 1
    hoursadj = 0

    data = open(rawFile, 'r')
    for line in data:
        if (lineNo == 1):
            lineNo = lineNo + 1
            continue
        temp_line = line.split(',')

        if (lineNo == 2):
            olddate = temp_line[0]
            lineNo = 0

        timelist = temp_line[1].split(":")
        hours = int(timelist[0])
        

        if (olddate != temp_line[0]):
            hoursadj = hours - 14
            olddate = temp_line[0]
              
        minutes = int(timelist[1])
        seconds = int(timelist[2])
        hours = hours - 5 - hoursadj
        if (hours >= 12):
            amorpm = "PM"
        else:
            amorpm = "AM"
            
        if (hours > 12):
            hours = hours-12
                
        trtime = str(hours) + ":" + str(format(minutes, '02d')) + ":"+ str(format(seconds, '02d'))+ " " + amorpm        
        single_result = []
        single_result.insert(0, ticker)
        single_result.insert(1, temp_line[0])
        
        single_result.insert(2, trtime)

        single_result.insert(3, temp_line[2])
        single_result.insert(4, temp_line[4])
        single_result.insert(5, temp_line[3])
        single_result.insert(6, temp_line[5])
        single_result.insert(7, temp_line[6])
        total_result.append(single_result)
    
    if (output == 'csv'):
        myFile = open('5MtsFile.csv', 'a', newline='')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(total_result)
    elif (output == 'db'):
        db_file = r'''C:\TickData2018\StooqData.accdb'''  #raw string, escape sequences are ignored

        conn = dbu.createDBConnection(db_file)
        c = conn.cursor()
        for row in total_result:
            sql = """INSERT INTO tbl5MtsRawFile VALUES ('%s', '%s', '%s','%s', '%s', '%s', '%s', '%s')""" \
            % (row[0], row[1], row[2],row[3], row[4], row[5], row[6], row[7])            
            c.execute(sql)
            conn.commit()
    else:
        print('output argument has to be either csv or db')

    if (output == 'db'):
        c.close()
        del c
        conn.close()
                
#    print("Program Completed")