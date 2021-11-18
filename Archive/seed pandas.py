import csv, sqlite3

con = sqlite3.connect("DataMart_db3.sqlite3") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
#cur.execute("CREATE TABLE t (col1, col2);") # use your column names here

with open('../dataset.csv', 'r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'], i['first_name'], i['last_name'], i['instrument'], i['singer']) for i in dr]

cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
con.commit()
con.close()