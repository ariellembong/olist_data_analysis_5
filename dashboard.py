import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium

# Load your datasets
rfm_df = pd.read_csv("rfm_df.csv")
most_revenue_regions = pd.read_csv("most_revenue_regions.csv")
top_customer_regions = pd.read_csv("top_customer_regions.csv")

# Title and description
st.title("Ecommerce Data Analysis Dashboard")
st.write("This dashboard allows you to explore customer purchasing behavior, revenue by region, and high-value customer locations.")

# Sidebar for filtering
st.sidebar.header("Filters")
top_n = st.sidebar.slider('Select Top N Customers by RFM Score', min_value=5, max_value=50, value=10)

# --- RFM Analysis ---
st.header("Most Valuable Customers (RFM)")
st.write(f"Displaying the top {top_n} valuable customers based on RFM analysis:")

# RFM calculations (simplified for dashboard)
# You can replace this part with the full RFM analysis from earlier.

st.dataframe(rfm_df)

# --- Revenue by Region ---

# Plot the revenue by region
fig, ax = plt.subplots()
most_revenue_regions.plot(kind='bar', x='seller_city', y='payment_value', ax=ax)
ax.set_title('Top 10 Revenue Generating Regions')
ax.set_xlabel('City')
ax.set_ylabel('Revenue')
st.pyplot(fig)

# --- Map of High-Value Customers ---
st.header("High-Value Customer Locations")
# Simplified version of map plotting using Folium
m = folium.Map(location=[-14.2350, -51.9253], zoom_start=4)

for index, row in top_customer_regions.iterrows():
    folium.Marker(
        location=[-23.5505, -46.6333],  # Example lat/lon for Sao Paulo
        popup=f"Customer ID: {row['customer_id']}\nRFM Score: {row['RFM_total_score']}",
        icon=folium.Icon(color="blue")
    ).add_to(m)

# Display the map
st_folium(m, width=700, height=500)

