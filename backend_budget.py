import sqlite3

class Database:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Spending (id INTEGER PRIMARY KEY, user TEXT, category TEXT, amount INTEGER, location TEXT, description TEXT, purchased TIMESTAMP)")
        self.conn.commit()

    def insert(self,user,category,amount,location,description,purchased):
        self.cur.execute("INSERT INTO Spending VALUES (NULL,?,?,?,?,?,?)",(user,category,amount,location,description,purchased)) #since table column id is a PRIMARY KEY passing NULL means python will assign the next available number to it
        self.conn.commit()
