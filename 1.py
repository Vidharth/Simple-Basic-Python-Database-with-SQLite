import sqlite3
import time
import datetime
import random
conn = sqlite3.connect("tutiorial.db")
c = conn.cursor()

def create_table():
   c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
   c.execute("INSERT INTO stuffToPlot VALUES(23423423, 'fnhuiedfu', 'iehjdfwejf', 5)")
   conn.commit()

def dynamic_data_entry():
   unix = time.time()
   date = str(datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S"))
   keyword = "Python"
   value = random.randrange(0,9)
   c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES(?, ?, ?, ?)", (unix, date, keyword, value))
   conn.commit()

def read_from_db():
   c.execute("SELECT * FROM stuffToPlot")
   for i in c.fetchall():
      print (i)
##   data = c.fetchall()
##   print(data)

read_from_db()
##create_table()
##data_entry()
##
##for i in range (0, 9):
##   dynamic_data_entry()
##   time.sleep(1)
   
c.close()
conn.close()             
