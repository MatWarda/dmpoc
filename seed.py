import pandas as pd
import sqlite3

con = sqlite3.connect("./Northwind_large.sqlite")
cols = ['OrderId', 'ProductId', 'UnitPrice', 'Quantity']
df = pd.read_sql_query("SELECT * FROM OrderDetail", con)
df_red = df[cols]

df_red.to_sql('OrderDetail', con, if_exists='replace', index=False, chunksize=15)
SQLdf = pd.read_sql_query("SELECT * from OrderDetail", con)
print('Data Mart table:')
print(SQLdf.head())
con.close()