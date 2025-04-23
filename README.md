[![Deployed on Render](https://img.shields.io/badge/Render-Live-blue)](https://ecommerce-analytics-api.onrender.com)

# 🛒 E-commerce Analytics API + Dashboard

**A full-stack e-commerce analytics tool built with FastAPI + Streamlit + Machine Learning.**  
It uses a real-world dataset of transactions to uncover business insights through SQL, clustering, and interactive dashboards.

---

## 🔧 Stack Overview

- ⚙️ Backend: **FastAPI** + **SQLite** + raw SQL queries
- 🎨 Frontend: **Streamlit** (interactive dashboard)
- 🤖 ML: **Customer Segmentation via KMeans**
- ☁️ Hosting: **Render** (API) + **Streamlit Cloud** (dashboard)

---

## 🚀 Features

- 🔝 Top customers by total revenue
- 📈 Daily revenue trends (with date filtering)
- 📦 Top-selling products
- 🌎 Sales by country *(coming soon)*
- 🧠 **Customer Segmentation** using RFM + KMeans
- 📊 Streamlit dashboard for visual insights

---

## 📡 API Access

✅ Live API (deployed on Render):  
🔗 [https://ecommerce-analytics-api.onrender.com/docs](https://ecommerce-analytics-api.onrender.com/docs)

### Available Endpoints:

- `/top-customers`
- `/daily-sales?start=YYYY-MM-DD&end=YYYY-MM-DD`
- `/top-products?limit=10`
- `/customer-segment?customer_id=12345`

---

## 🎨 Streamlit Dashboard

✅ Live App:  
🔗 [https://ecommerce-analytics-api.streamlit.app](https://ecommerce-analytics-api.streamlit.app)

Interactive dashboard built on top of the FastAPI API. Powered by real-time data and machine learning.

### 📊 Views Included:

- **Top Customers** – bar chart + data table of top 10 spenders
- **Daily Sales** – filterable line chart of daily revenue
- **Customer Segmentation** – enter a customer ID to view:
  - Recency, Frequency, Monetary value
  - Assigned cluster (e.g., "Loyal", "At Risk", "High Value")

---

## 📘 Dataset

📦 [Kaggle: E-Commerce Data](https://www.kaggle.com/datasets/carrie1/ecommerce-data)  
UK-based online retail transaction dataset with product-level invoice data.

---

## Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/ecommerce-analytics-api.git
   cd ecommerce-analytics-api