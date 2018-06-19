'''
Created on Jun 7, 2018

@author: karsu
'''
import pyodbc

def createDBConnection(db_file):
    user = 'admin'
    password = ''   
    odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;UID=%s;PWD=%s' %\
                (db_file, user, password)    #string variable formatted according to pyodbc specs
                
    try:
        conn = pyodbc.connect(odbc_conn_str)
    #            print("connection made")
    except Exception as e:
        print('Database connection is failed')
        print(e)               
    c = conn.cursor()
    list1 = [conn, c]
    return list1