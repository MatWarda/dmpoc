import pandas as pd
import sqlite3

con = sqlite3.connect("./DM4.sqlite3")
cols = ['OrderId', 'ProductId', 'UnitPrice', 'Quantity']
df = pd.read_csv('dataset.csv', sep=";", usecols=cols, nrows=15)
#df = pd.read_csv('dataset.csv', sep=";")
df.to_sql('OrderDetail', con, if_exists='replace', index=False, chunksize=15)
SQLdf = pd.read_sql_query("SELECT * from OrderDetail", con)
print('Data Mart table:')
print(SQLdf.head())
con.close()