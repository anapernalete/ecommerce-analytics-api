from fastapi import FastAPI
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
    query = """
    SELECT CustomerID, SUM(Quantity * UnitPrice) AS TotalSpent
    FROM transactions
    GROUP BY CustomerID
    ORDER BY TotalSpent DESC
    LIMIT 10;
    """
    
    return {"data": run_query(query)}