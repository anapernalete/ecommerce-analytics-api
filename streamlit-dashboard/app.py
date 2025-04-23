import streamlit as st
import requests
import pandas as pd

API_URL = "https://ecommerce-analytics-api.onrender.com"

st.title("E-commerce Dashboard")

# Sidebar
option = st.sidebar.selectbox("Select a view", [
    "Top Customers",
    "Daily Sales",
    "Customer Segmentation"
])


# Top Customers
if option == "Top Customers":
    st.header("Top Customers by Revenue")
    
    response = requests.get(f"{API_URL}/top-customers")
    if response.status_code == 200:
        data = pd.DataFrame(response.json()["data"], columns=["CustomerID", "TotalSpent"])
        st.dataframe(data)
        st.bar_chart(data.set_index("CustomerID"))
    else:
        st.error("Failed to fetch data from API")
        
elif option == "Daily Sales":
    st.header("Daily Sales Revenue")
    
    # Select date range
    start = st.date_input("Start date", pd.to_datetime("2010-12-01"))
    end = st.date_input("End date", pd.to_datetime("2011-01-31"))
    
    if start < end:
        response = requests.get(f"{API_URL}/daily-sales", params={"start": str(start), "end": str(end)})
        if response.status_code == 200:
            data = pd.DataFrame(response.json()["data"], columns=["Date", "Revenue"])
            data["Date"] = pd.to_datetime(data["Date"])
            st.line_chart(data.set_index("Date"))
            st.dataframe(data)
        else:
            st.error("Failed to fetch daily sales data")
    else:
        st.warning("End date must be after start date")
        
elif option == "Customer Segmentation":
    st.header("Customer Segmentation")
    
    customer_id = st.number_input("Enter Customer ID", min_value=0, step=1)
    
    if st.button("Get Segment"):
        try:
            st.write("Sending request to API...")
            st.write(f"Customer ID: {customer_id}")

            response = requests.get(f"{API_URL}/customer-segment", params={"customer_id": customer_id})
            st.write("Response received")
            st.write("Raw JSON:", response.json())

            if response.status_code == 200:
                result = response.json()
                if "error" in result:
                    st.error(result["error"])
                else:
                    st.write("Parsed result:", result)
                    segment_labels = {
                        0: "Loyal",
                        1: "At Risk",
                        2: "High Value",
                        3: "New"
                    }
                    segment_name = segment_labels.get(result["segment"], "Unknown")
                    
                    st.success(f"Segment: {segment_name}")
                    st.write(f"Recency: {result['recency']} days")
                    st.write(f"Frequency: {result['frequency']} purchases")
                    st.write(f"Monetary Value: ${result['monetary']}")
                    
            else:
                st.error("Failed to fetch data from API")
                st.write(" Response code:", response.status_code)

        except Exception as e:
            st.error(f"Error: {e}")