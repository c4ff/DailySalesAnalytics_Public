import sqlite3
import pandas as pd

conn = sqlite3.connect("data/database/daily_sales_analysis.db")

query = """
SELECT *,
    CASE
        WHEN strftime('%w', "Date") = '0' THEN 'Sunday'
        WHEN strftime('%w', "Date") = '1' THEN 'Monday'
        WHEN strftime('%w', "Date") = '2' THEN 'Tuesday'
        WHEN strftime('%w', "Date") = '3' THEN 'Wednesday'
        WHEN strftime('%w', "Date") = '4' THEN 'Thursday'
        WHEN strftime('%w', "Date") = '5' THEN 'Friday'
        WHEN strftime('%w', "Date") = '6' THEN 'Saturday'
    END AS weekday
FROM daily_sales;
"""

df = pd.read_sql_query(query, conn)

df.to_csv(
    "data/cleaned/daily_sales_powerbi.csv",
    index=False
)

conn.close()

print("CSV exported successfully!")