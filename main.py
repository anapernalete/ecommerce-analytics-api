import os
from fastapi import FastAPI
from fastapi import Query
import pandas as pd
import sqlite3
import joblib

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

@app.get("/customer-segment")
def get_customer_segment(customer_id: int = Query(...)):
    kmeans_model = joblib.load("models/kmeans_model.pkl")
    scaler = joblib.load("models/rfm_scaler.pkl")
    
    #Load transactions
    conn = sqlite3.connect("ecommerce.db")
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()
    
    df = df.dropna(subset=["CustomerID", "InvoiceDate", "InvoiceNo", "Quantity", "UnitPrice"])
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    
    if customer_id not in df["CustomerID"].unique():
        return {"error": f"Customer ID {customer_id} not found"}
    
    latest_date = df["InvoiceDate"].max()
    cust_df = df[df["CustomerID"] == customer_id]
    
    recency = (latest_date - cust_df["InvoiceDate"].max()).days
    frequency = cust_df["InvoiceNo"].nunique()
    monetary = (cust_df["Quantity"] * cust_df["UnitPrice"]).sum()
    
    rfm_features = pd.DataFrame([{
        "Recency": recency,
        "Frequency": frequency,
        "Monetary": monetary
    }])
    
    rfm_scaled = scaler.transform(rfm_features)
    segment = int(kmeans_model.predict(rfm_scaled)[0])
    
    return {
        "customer_id": customer_id,
        "recency": recency,
        "frequency": frequency,
        "monetary": round(monetary, 2),
        "segment": segment
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)