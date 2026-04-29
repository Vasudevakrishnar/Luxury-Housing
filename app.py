import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from cleaning import clean_data

st.title("🏠 Real Estate Analytics Dashboard")

# Load & clean data
df = clean_data()

st.subheader("📊 Cleaned Dataset")
st.dataframe(df)

# ----------------- FILTERS -----------------
st.sidebar.header("Filters")

location = st.sidebar.selectbox("Select Location", df["location"].unique())
filtered_df = df[df["location"] == location]

# ----------------- METRICS -----------------
st.subheader("📌 Key Metrics")

st.metric("Average Price", f"{filtered_df['price'].mean():,.0f}")
st.metric("Average Area", f"{filtered_df['area'].mean():,.0f}")
st.metric("Avg Price per Sqft", f"{filtered_df['price_per_sqft'].mean():,.0f}")

# ----------------- VISUALIZATION -----------------
st.subheader("📈 Price Distribution")

fig, ax = plt.subplots()
sns.histplot(filtered_df["price"], kde=True, ax=ax)
st.pyplot(fig)

# Area vs Price
st.subheader("📊 Area vs Price")

fig2, ax2 = plt.subplots()
sns.scatterplot(x=filtered_df["area"], y=filtered_df["price"], ax=ax2)
st.pyplot(fig2)

# ----------------- INSIGHTS -----------------
st.subheader("🔍 Insights")

st.write("""
- Larger houses generally have higher prices  
- Location significantly impacts property value  
- Price per square foot helps compare properties fairly  
- Older houses tend to have lower valuation  
""")