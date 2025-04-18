from fastapi import FastAPI
from fastapi import Query
import sqlite3

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