import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium

# Load datasets
rfm_df = pd.read_csv("rfm_df.csv")
most_revenue_regions = pd.read_csv("most_revenue_regions.csv")
top_customer_regions = pd.read_csv("top_customer_regions.csv")

# Title and description
st.title("Olist Ecommerce Data Analysis Dashboard")

# RFM Analysis


st.header("Customers Quality (RFM) Distribution")

fig, ax = plt.subplots(figsize=(8, 6))
rfm_df['RFM_total_score'].value_counts().sort_index().plot(kind='bar', ax=ax)
ax.set_title('Distribution of RFM Scores')
ax.set_xlabel('RFM Score')
ax.set_ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)


# revenue by region
st.header("Revenue by Region")

top_n = st.selectbox("Choose how many top revenue regions to display", [3, 5, 10])

top_revenue_regions = most_revenue_regions.head(top_n)

fig, ax = plt.subplots()
top_revenue_regions.head(10).plot(kind='bar', x='seller_city', y='payment_value', ax=ax)
ax.set_title(f'Top {top_n} Revenue Generating Regions')
ax.set_xlabel('City')
ax.set_ylabel('Revenue')
st.pyplot(fig)

# High-value customers Locations
st.header("High-Value Customers Locations")
# Simplified version of map plotting using Folium
m = folium.Map(location=[-14.2350, -51.9253], zoom_start=4)

for _, row in top_customer_regions.iterrows():
    folium.Marker(
        location=[-23.5505, -46.6333], 
        popup=f"{row['geolocation_city']}, {row['geolocation_state']}: {row['high_value_customers']} high-value customers",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

st_folium(m, width=700, height=500)

