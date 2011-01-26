import os.path
import sqlite3

dbpath = os.path.join(os.path.dirname(__file__), '../db/pymin.db')
    
def query_select(stet,row=None):
     con = sqlite3.connect(dbpath)
     cur = con.cursor()
     cur.execute(stet)
     if row == None:
	  a = cur.fetchone()
	  return a
     elif row == 'all':
	  a = cur.fetchall()
	  return a

def query_insert(stet):
    con = sqlite3.connect(dbpath)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(stet)
    con.commit()
    con.close()