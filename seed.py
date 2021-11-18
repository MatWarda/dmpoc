import pandas as pd
import sqlite3


con = sqlite3.connect("./DM004.sqlite3")
#cols = ['id', 'instrument', 'singer']
#df = pd.read_csv('dataset.csv', sep=";", usecols=cols, nrows=15)
df = pd.read_csv('dataset.csv', sep=";", nrows=15)
df.to_sql('DMmigration_musician', con, if_exists='replace', index=False, chunksize=15)
#con.execute("SELECT * FROM DMmigration_musician").fetchall()
SQLdf = pd.read_sql_query("SELECT * from DMmigration_musician", con)
print('SQLite table read:')
print(SQLdf.head())
con.close()
