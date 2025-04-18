[![Deployed on Render](https://img.shields.io/badge/Render-Live-blue)](https://ecommerce-analytics-api.onrender.com)

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
- 📊 Streamlit dashboard for visual insights

## 📡 API Access
- ✅ Live API (deployed on Render):  
  [`https://ecommerce-analytics-api.onrender.com/docs`](https://ecommerce-analytics-api.onrender.com/docs)

- ✅ Endpoints:
  - `/top-customers`
  - `/daily-sales?start=YYYY-MM-DD&end=YYYY-MM-DD`
  - `/top-products?limit=10`

## 🎨 Streamlit Dashboard
An interactive dashboard built on top of the FastAPI backend. It fetches data from the deployed API and visualizes it with Streamlit.

- ✅ Live Dashboard:  
  [`https://ecommerce-analytics-api.streamlit.app`](https://your-username.streamlit.app)

📊 Current Dashboard Views
- Top Customers
Bar chart + data table of the top 10 spenders

- Daily Sales
Line chart of daily revenue with a filterable date range

## 📊 Tech Stacks
- Backend: Python, FastAPI, SQLite
- Data Layer: Raw SQL
- Frontend: Streamlit
- Hosting: Render (API) + Streamlit Cloud (Dashboard)

## 📘 Dataset
[`https://www.kaggle.com/datasets/carrie1/ecommerce-data`](https://ecommerce-analytics-api.onrender.com/docs)