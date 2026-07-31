"""
Clean raw daily restaurant sales data for downstream analysis.

The script selects analysis-ready fields, validates dates, converts currency
values to numeric types, standardizes order counts, and exports the cleaned
dataset to ``data/cleaned/daily_sales_cleaned.csv``.
"""

import pandas as pd


# Columns we want in our final analytics dataset remove unnecessary columns 
# (ie columns that are not used such as column related to delivery orders we do not deliver atm)
columns_to_keep = [
    "Date",
    "Closed Orders",
    "Gross Sales",
    "Discounts",
    "Net Sales",
    "Fees",
    "Taxes",
    "Service Tips",
    "Amount Receivable",
    "Total Refunds",
    "Net Sales Refunds",
    "Taxes Refunds",
    "Service Tips Refunds"
]


# Columns that contain money values 
# These columns are cleaned because it has $ and , which caused Python to treat them as strings instead of floats
# We want floats because we want to keep the decimal values instead of int which removes the decimals

money_columns = [
    "Gross Sales",
    "Discounts",
    "Net Sales",
    "Fees",
    "Taxes",
    "Service Tips",
    "Amount Receivable",
    "Total Refunds",
    "Net Sales Refunds",
    "Taxes Refunds",
    "Service Tips Refunds"
]


# Load raw CSV

df = pd.read_csv(
    "data/raw/daily_details_2025-01-13_to_2026-01-13.csv",
    skiprows=1
)

#remove the last row becasue it's messing up the datetime conversion
df = df[pd.to_datetime(df["Date"], errors='coerce').notna()]


# Convert Date column
# I noticed the date column needs to be treated separately because it is in string but we want datetime

df["Date"] = pd.to_datetime(df["Date"])


# Clean money columns
# See here we removed the dollar signs and the commas so now strings become floats and we can use math in SQLite

for column in money_columns:
    df[column] = (
        df[column]
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

#after the test commands I found 1 missing item in column: closed orders so 
#this following command will locate it
#print(df[df["Closed Orders"].isna()])
#I found the problem, it was showing a missing value so now I will conver it to 0
df["Closed Orders"] = df["Closed Orders"].fillna(0)
#I noticed closed orders column is in float but it only contains integers
#I will now conver all to integers
df["Closed Orders"] = df["Closed Orders"].astype(int)
# Keep only selected columns

df = df[columns_to_keep]
df.to_csv("data/cleaned/daily_sales_cleaned.csv", index=False)





# print(df.head())
# print(df.shape)
# print(df.dtypes)
#print(df.isna().sum())
