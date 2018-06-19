import pyodbc
import datetime
import sys

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
#    c = conn.cursor()
#    list1 = [conn, c]
    return conn

def getTableColumns(conn, table_name):
    c = conn.cursor()    
    sql = """ SELECT * FROM """
    sql = sql + table_name
    c.execute(sql)
    columns = [column[0] for column in c.description]
    return columns


def getTableColumnsDetails(conn, table_name):
    c = conn.cursor()    
    sql = """ SELECT * FROM """
    sql = sql + table_name
    c.execute(sql)
    return c.description


def getAllTablesInDB(conn):
    c = conn.cursor()
    tables = [table for table in c.tables() if table[3] == 'TABLE']    
    return tables

def getAllViewsInDB(conn):
    c = conn.cursor()
    views = [table for table in c.tables() if table[3] == 'VIEW']    
    return views

def get_all_recs(conn, tablename):
    
    c = conn.cursor()
    sql = """ SELECT * FROM """
    sql = sql + tablename
    c.execute(sql)

    columns = [column[0] for column in c.description]
    
    recs = []
    for row in c.fetchall():
        recs.append(dict(zip(columns, row)))
    
    return recs

if __name__ == '__main__': 
    pass
