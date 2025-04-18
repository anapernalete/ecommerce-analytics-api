import os
from fastapi import FastAPI
from fastapi import Query
import pandas as pd
import sqlite3

if not os.path.exists("ecommerce.db"):
    df = pd.read_csv("data.csv", encoding="ISO-8859-1")
    df = df.dropna(subset=["CustomerID", "InvoiceNo", "InvoiceDate", "StockCode"])
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    conn = sqlite3.connect("ecommerce.db")
    df.to_sql("transactions", conn, if_exists="replace", index=False)
    conn.close()

app = FastAPI()

def run_query(query, params=()):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    
    return result

@app.get("/top-customers")
def top_customers():
    with open("queries/top-customers.sql") as f:
        query = f.read()
    return {"data": run_query(query)}

@app.get("/sales_by_country")
def sales_by_country():
    with open("queries/sales_by_country.sql") as f:
        query = f.read()
    return {"data": run_query(query)}

@app.get("/daily-sales")
def daily_sales(start: str = Query(...), end: str = Query(...)):
    with open("queries/daily_sales.sql") as f:
        query = f.read()
    return {"data": run_query(query, (start, end))}

@app.get("/top-products")
def top_products(limit: int = 10):
    with open("queries/top_products.sql") as f:
        query = f.read()
    return {"data": run_query(query, (limit))}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)