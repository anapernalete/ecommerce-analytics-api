import pandas as pd
import sqlite3

# Load dataset
df = pd.read_csv('data.csv', encoding="ISO-8859-1")

# Basic cleaning
df = df.dropna(subset=['CustomerID', 'InvoiceNo', 'InvoiceDate', 'StockCode'])
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

#Save to SQLite
conn = sqlite3.connect('ecommerce.db')
df.to_sql('transactions', conn, if_exists='replace', index=False)
conn.close()

print("Database created successfully")