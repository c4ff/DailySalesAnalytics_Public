import pandas as pd
import sqlite3

#load the correct, cleaned CSV
df = pd.read_csv("data/cleaned/daily_sales_cleaned.csv")

#create a connection to the SQLite database
conn = sqlite3.connect("data/database/daily_sales_analysis.db")

#load the df dataframe into SQLite table
df.to_sql("daily_sales", conn, if_exists="replace", index=False)

# print(df.head())
# print(df.shape)


#test to see the data are actually loaded
#check tables inside database
# print("Database test:")

# cursor = conn.cursor()

# cursor.execute(
#     "SELECT name FROM sqlite_master WHERE type='table';"
# )

# print(cursor.fetchall())

#finished so I close the connection
conn.close()