'''
Created on Jun 4, 2018

@author: karsu
'''
#z tbl5MtsRawFile
import os
#import pyodbc
import proc1file
import csv
#output = 'csv'
output = 'db'


    
#dirname = "C:\\TickData2018\\nysestocks_temp\\"
dirname = ""
   
if (output == 'csv'):
    f1 = open('5MtsFile.csv', 'w')
    hdrData = ["Ticker", "CurDate", "CurTime",
           "Open", "Low", "High", "Close", "Volume"]   
    myFile = open('5MtsFile.csv', 'w', newline='')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerow(hdrData)
        
# if this CSV file has to be imported into MS Access DB, you have to first save this as MS Excel Book in Excel
 
fileNum = 0

selected_tickers_file = "selectedTickers.csv"

selectedTickers = csv.reader(open(selected_tickers_file, 'r'), delimiter=',')

for item in selectedTickers:
#    print(item)
    ticker_name = item[1]
    print(ticker_name)
#        for x in os.listdir(dirname):
    fname = dirname + ticker_name + ".us.txt"
    if (os.path.isfile(fname)) :
        fileNum = fileNum+1
    #    if (fileNum == 2):
    #        break
#        print(fname)
        proc1file.getSingleFileData(fname,output)
print('Program Completed')            
