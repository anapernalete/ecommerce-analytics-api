import sqlite3
import pandas as pd
from sklearn.cluster import KMeans
import joblib
import os

# Connect to database
conn = sqlite3.connect("ecommerce.db")
df = pd.read_sql_query("SELECT * FROM transactions", conn)
conn.close()

# Clean missing CustomerID
df = df.dropna(subset=["CustomerID", "InvoiceDate", "InvoiceNo", "Quantity", "UnitPrice"])
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Latest purchase date for Recency calculation
latest_date = df["InvoiceDate"].max()

# RFM table
rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (latest_date - x.max()).days,
    "InvoiceNo": "nunique",
    "Quantity": lambda x: (x * df.loc[x.index, "UnitPrice"]).sum()
}).reset_index()

rfm.columns = ["CustomerID", "Recency", "Frequency", "Monetary"]
rfm = rfm[["CustomerID", "Recency", "Frequency", "Monetary"]]

# Normalize features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[["Recency", "Frequency", "Monetary"]])

# KMeans clustering
model = KMeans(n_clusters=4, random_state=42)
rfm["Segment"] = model.fit_predict(rfm_scaled)

# Save model and scaler
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/kmeans_model.pkl")
joblib.dump(scaler, "models/rfm_scaler.pkl")
rfm.to_csv("models/rfm_with_segments.csv", index=False)

print("Customer segmentation model has been trained and saved")