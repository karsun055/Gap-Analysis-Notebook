'''
Program Name - chartDisplay.py

Created on Jun 14, 2018

@author: karsu
'''
from tkinter import *
from tkinter import ttk
import datetime
import io_5MtsBaseForAnalysisSorted as base5
import io_StooqCrossTabTable as sct
import db_utils as dbu
import plotCSChartSingle as plot
import read_selected_stooq_cross_tab as rct
import os


class Application(Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        root.minsize(width=600, height=800)
        root.resizable(width=0, height=0)
        self.grid()
        self.create_widgets()
    
    
    def create_widgets(self):
#        root = Tk()

        self.image = PhotoImage(file="cs1.png")
        self.label1 = ttk.Label(image=self.image)
        self.label1.grid(row=22, column = 0, columnspan = 8, padx=5, pady = 5)

        self.tv = ttk.Treeview(root,selectmode='browse')
        self.tv = ttk.Treeview(self, height=20)
        self.tv.place(x=30, y=95)

        self.vsb = ttk.Scrollbar(root, orient="vertical", command=self.tv.yview)
        self.vsb.place(x=30+656+2, y=10, height=400+20)
        
        self.tv.configure(yscrollcommand=self.vsb.set)

        self.tv['columns'] = ('Ticker', 'Tr Date')
        self.tv.heading("#0",text="Time", anchor = "w")
        self.tv.column('#0', stretch=NO, width=5, anchor='w')
        self.tv.heading('Ticker', text='Ticker')
        self.tv.column('Ticker', anchor='center', width = 80)
        self.tv.heading('Tr Date', text='Tr Date')
        self.tv.column('Tr Date', anchor='center', width = 612)
        self.tv.bind('<ButtonRelease-1>', self.select_item)
        self.tv.grid(row=1, column = 0, columnspan = 30, padx=5, pady = 5)
        self.treeview = self.tv
        
        ttk.Style().configure("Treeview", font = ('',11), background="#383838#",
        foreground="white", fieldbackground = "yellow")

        db_file = 'StooqDataAnalysis.accdb'  
        db_file = os.path.abspath(db_file)
        conn = dbu.createDBConnection(db_file)

        in_recs = sct.get_all_StooqCrossTabTable_recs(conn)
        print(len(in_recs))
        
        for rec in in_recs:
#            print(str(rec['CurDate']))
            datestr = str(rec['CurDate'])[:10]
#            print(datestr)
            year,month,day = str(datestr).split("-")
#            print(year,month,day)
            ticker1 = rec['Ticker']
            self.tv.insert("", "end",  values = (ticker1, datetime.date(year = int(year), month=int(month), day=int(day))))

             
    def select_item(self, a):
        test_str_library = self.tv.item(self.tv.selection())  # gets all the values of selected row
#        print('The test str = ', type(test_str_library), test_str_library, '\n') #prints a dictionary of the selected row
        item = self.tv.selection()[0] # which row did you click on
#        print('item clicked', item) # variable that represents the row you clicked on
        ticker_selected = self.tv.item(item)['values'][0] # prints the first value of the values list
        date_selected = self.tv.item(item)['values'][1]
#        print(ticker_selected, date_selected)

        myfile="cs2.png"
        if os.path.isfile(myfile):
            os.remove(myfile)
            print('cs2.png removed)')

        rct.get_selected_cross_tab_rec(ticker_selected, date_selected)

        self.image2 = PhotoImage(file=myfile)
#        self.label1.image = image
#        self.label1.grid(row=22, column = 0, columnspan = 8, padx=5, pady = 5)
        self.label1.configure(image=self.image2)
        self.label1.image=self.image2

        
root = Tk()
Application(root)
root.mainloop()

#        the following is the test data to fillup the treeview widget
        #=======================================================================
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=3, day=15)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=16)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=17)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=3, day=15)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=16)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=17)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=3, day=15)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=16)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=17)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=3, day=15)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=16)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=17)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=3, day=15)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=16)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=17)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=3, day=15)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=16)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=17)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=3, day=15)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=16)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=17)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=3, day=15)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=16)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=17)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=3, day=15)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=16)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=17)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=3, day=15)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=16)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=17)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=3, day=15)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=16)))
        # self.tv.insert("", "end",  values = ("A", datetime.date(year=2018, month=6, day=17)))
        #=======================================================================
                    
  
    
            
 
