from tkinter import *
from tkinter import ttk
from backend_budget import Database
from datetime import datetime

# database = Database("TestDB")
database = Database("TrackingDB.db")

class Window(object):

    def __init__(self,window):
        self.window = window
        self.window.wm_title("BudgetTracker")

        l1 = Label(window,text='Select User: ')
        l1.grid(row=0, column=0)

        user = ""

        self.user=StringVar()
        self.e1 = ttk.Combobox(window, state="readonly", textvariable=self.user)
        self.e1.grid(row=0,column=1)
        self.e1['values']=('Jacqui','Noise')

        l2 = Label(window,text='Select category: ')
        l2.grid(row=1, column=0)

        category = ""

        self.category=StringVar()
        self.e2 = ttk.Combobox(window, state='readonly', textvariable=self.category)
        self.e2.grid(row=1,column=1)
        self.e2['values']=('Groceries','Restaurants','Booze','Activities','Misc purchases')

        l3 = Label(window,text='Purchase amount: $')
        l3.grid(row=2, column=0)

        self.amount=StringVar()
        self.e3 = Entry(window,textvariable=self.amount)
        self.e3.grid(row=2,column=1)

        l4 = Label(window,text='Purchase location: ')
        l4.grid(row=3, column=0)

        self.location=StringVar()
        self.e4 = Entry(window,textvariable=self.location)
        self.e4.grid(row=3,column=1)

        l5 = Label(window,text='Purchase description: ')
        l5.grid(row=4, column=0)

        self.description=StringVar()
        self.e5 = Entry(window,textvariable=self.description)
        self.e5.grid(row=4, column=1)

        l6 = Label(window,text='Year: ')
        l6.grid(row=6,column=0)
        l7 = Label(window,text='Month: ')
        l7.grid(row=7,column=0)
        l8 = Label(window,text='Day: ')
        l8.grid(row=8,column=0)

        year = ""
        month = ""
        day = ""

        self.year=StringVar()
        self.month=StringVar()
        self.day=StringVar()
        self.e6 = ttk.Combobox(window, state="readonly", textvariable=self.year)
        self.e7 = ttk.Combobox(window, state="readonly", textvariable=self.month)
        self.e8 = ttk.Combobox(window, state="readonly", textvariable=self.day)
        self.e6.grid(row=6,column=1)
        self.e7.grid(row=7,column=1)
        self.e8.grid(row=8,column=1)
        self.e6['values']=('2018','2019')
        self.e7['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
        self.e8['values']=('01','02','03','04','05','06','07','08','09','10',
            '11','12','13','14','15','16','17','18','19','20',
            '21','22','23','24','25','26','27','28','29','30','31')

        b1 = Button(window,text='Submit', width=12, command=self.submit_command)
        b1.grid(row=9,column=0)

    def submit_command(self):
        if len(self.user.get()) >= 1:
            if len(self.category.get()) >= 1:
                try:
                    entered_date = self.year.get() + ' ' + self.month.get() + ' ' + self.day.get()
                    purch_date = datetime.strptime(entered_date, '%Y %B %d')
                    amount_int=int(self.amount.get())
                    database.insert(self.user.get(),self.category.get(),amount_int,self.location.get(),self.description.get(),purch_date)
                    self.e1.delete(0,END)
                    self.e2.delete(0,END)
                    self.e3.delete(0,END)
                    self.e4.delete(0,END)
                    self.e5.delete(0,END)
                    self.e6.delete(0,END)
                    self.e7.delete(0,END)
                    self.e8.delete(0,END)
                    print("Data entered")
                except ValueError:
                    print("Amount must be number")
            else:
                print("Select a category")
        else:
            print("Select a user")


window = Tk()
Window(window)
window.mainloop()
