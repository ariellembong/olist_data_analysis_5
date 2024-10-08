import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium

# Load your datasets
rfm_df = pd.read_csv("rfm_df.csv").head()
most_revenue_regions = pd.read_csv("most_revenue_regions.csv")
top_customer_regions = pd.read_csv("top_customer_regions.csv")

# Title and description
st.title("Ecommerce Data Analysis Dashboard")
st.write("This dashboard allows you to explore customer purchasing behavior, revenue by region, and high-value customer locations.")


# --- RFM Analysis ---
st.header("Most Valuable Customers (RFM)")


# RFM calculations (simplified for dashboard)
# You can replace this part with the full RFM analysis from earlier.
fig, ax = plt.subplots(figsize=(8, 8))
rfm_df['RFM_total_score'].value_counts().sort_index().plot(kind='bar', ax=ax)
ax.set_title('Distribution of RFM Scores')
ax.set_xlabel('RFM Score')
ax.set_ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the figure using Streamlit
st.pyplot(fig)

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

