import streamlit as st
import plotly.express as px
import pandas as pd
import requests

# --- App Title ---
st.title("🦠 COVID-19 Global Dashboard")

# --- Fetch Data from API ---
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)
data = response.json()

# --- Convert to DataFrame ---
df = pd.DataFrame(data)
df = df[["country", "cases", "deaths", "recovered", "active", "population"]]

# --- Sidebar Controls ---
st.sidebar.header("Filter Options")
sort_by = st.sidebar.selectbox("Sort by:", ["cases", "deaths", "recovered", "active"])
top_n = st.sidebar.slider("Select number of countries:", 5, 20, 10)

# --- Data Sorting ---
top_countries = df.sort_values(by=sort_by, ascending=False).head(top_n)

# --- Display Data Table ---
st.subheader(f"Top {top_n} countries by {sort_by}")
st.dataframe(top_countries)

# --- Plotly Bar Chart ---
fig = px.bar(
    top_countries,
    x="country",
    y=sort_by,
    color="country",
    title=f"Top {top_n} Countries by {sort_by.capitalize()}",
    text=sort_by,
)
st.plotly_chart(fig, use_container_width=True)

# --- Pie Chart ---
st.subheader("Distribution of Selected Metric")
pie_fig = px.pie(
    top_countries,
    values=sort_by,
    names="country",
    title=f"{sort_by.capitalize()} Distribution among Top {top_n} Countries",
)
st.plotly_chart(pie_fig, use_container_width=True)

# --- Footer ---
st.markdown("---")
st.caption("Data source: https://disease.sh | Dashboard created with Streamlit and Plotly Express")
