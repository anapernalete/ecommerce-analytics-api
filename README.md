# 🛒 E-commerce Analytics API

Full-stack e-commerce analytics tool built with **FastAPI** and **Streamlit**.  
It uses an e-commerce transactions dataset to expose key business insights through:

- A lightweight **FastAPI backend** with SQL-powered endpoints
- An interactive **Streamlit dashboard** to explore and visualize the data

The backend handles all data processing through raw SQL queries on a SQLite database.
The frontend consumes those endpoints to display charts, tables, and filters for key metrics like customer spending and daily revenue.

The goal is to provide clean, reusable endpoints for common e-commerce analytics tasks, such as identifying top customers, tracking daile revenue, and evaluating sales by country or product.

## 🚀 Features
- 🔝 Top customers by total revenue
- 🌎 Sales by country
- 📈 Daily revenue trends
- 📦 Top-selling products
-  📊 Streamlit dashboard for visual insights

## 📡 API Access
- ✅ Currently runs locally at:
  http://127.0.0.1:8000/docs

## 📊 Tech Stacks
- Backend: Python, FastAPI, SQLite
- Data Layer: Raw SQL
- Frontend: Streamlit or React
- Hosting: 

## 🎨 Streamlit Dashboard
Simple, interactive dashboard built on top of the FastAPI backend. It fetches data from the API endpoints and visualizes it with charts, tables, and filters.

📊 Current Dashboard Views
- Top Customers
View the top 10 customers ranked by total revenue (bar chart + table)

- Daily Sales
Filter sales by date range and view total revenue over time (line chart)

## 🔧 How to Run
- Start the FastAPI server 
  - uvicorn main:app --reload
- Run the Streamlit app
  - cd streamlit-dashboard 
  - streamlit run app.py
- Open browser at:
  - http://localhost:8501

## 📘 Dataset
https://www.kaggle.com/datasets/carrie1/ecommerce-data