import pandas as pd
import sqlite3
import configparser

"""importing variables from config"""
config = configparser.RawConfigParser()
config.read("configfile.ini")

datamart_name = config.get('data_mart', 'name')
datamart_type = config.get('data_mart', 'output_type')
datamart_file = (datamart_name + '.' + datamart_type)
source_table = config.get('source', 'table')

first_n_rows = config.get('data_mart', 'first_n_rows')
last_n_rows = config.get('data_mart', 'last_n_rows')

column_names = config.get('data_mart', 'model_manual')
cols = column_names.split()


"""read data from source and process"""
con = sqlite3.connect("./Northwind_large.sqlite")
df = pd.read_sql_query("SELECT * from " + source_table, con)
df_red = df[cols]

if first_n_rows:
    df_red = df_red.head(int(first_n_rows))
elif last_n_rows:
    df_red = df_red.head(int(last_n_rows))


"""create target and write"""
cxn = sqlite3.connect(datamart_file)
df_red.to_sql(source_table, cxn, if_exists='replace', index=False, chunksize=15)
SQLdf = pd.read_sql_query("SELECT * from " + source_table, cxn)
cxn.close()

print('Data Mart table:')
print(SQLdf.head())
