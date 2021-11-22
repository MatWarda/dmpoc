import pandas as pd
import sqlite3
import configparser


config = configparser.RawConfigParser()
config.read("configfile.ini")
datamart_name = config.get('data_mart', 'name')
datamart_type = config.get('data_mart', 'output_type')
datamart_file = (datamart_name + '.' + datamart_type)

column_names = config.get('data_mart', 'model_manual')
cols = column_names.split()

con = sqlite3.connect("./Northwind_large.sqlite")
df = pd.read_sql_query("SELECT * FROM OrderDetail", con)
df_red = df[cols] #check if change in configfile has an effect
con.close()


cxn = sqlite3.connect(datamart_file)
df_red.to_sql('OrderDetail', cxn, if_exists='replace', index=False, chunksize=15)
SQLdf = pd.read_sql_query("SELECT * from OrderDetail", cxn)
print('Data Mart table:')
print(SQLdf.head())
cxn.close()