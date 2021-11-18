import pandas as pd
import sqlite3


con = sqlite3.connect("./DM002.sqlite3")
cols = ['id', 'instrument', 'singer']
df = pd.read_csv('dataset.csv', sep=";", usecols=cols, nrows=15)
#df = pd.read_csv('dataset.csv', sep=";")
df.to_sql('DMmigration_musician', con, if_exists='replace', index=False, chunksize=15)
#con.execute("SELECT * FROM DMmigration_musician").fetchall()
con.close()
