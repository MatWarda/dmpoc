import pandas as pd
import sqlite3

con = sqlite3.connect("./Northwind_large.sqlite")
df = pd.read_sql_query("SELECT * FROM OrderDetail", con)
cols = ['OrderId', 'ProductId', 'UnitPrice', 'Quantity']
df_red = df[cols]
con.close()


cxn = sqlite3.connect("./DataMart.sqlite3")
df_red.to_sql('OrderDetail', cxn, if_exists='replace', index=False, chunksize=15)
SQLdf = pd.read_sql_query("SELECT * from OrderDetail", cxn)
print('Data Mart table:')
print(SQLdf.head())
cxn.close()