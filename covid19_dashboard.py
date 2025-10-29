import streamlit as st
import plotly.express as px
import pandas as pd
import requests
import os
import matplotlib.pyplot as plt
import seaborn as sns   

st.set_page_config(page_title="COVID-19 Dashboard", page_icon= ":bar_chart:" ,layout="wide")
st.title(":bar_chart: COVID-19 Global Dashboard") 

os.chdir(r"C:\Users\Admin\OneDrive\Desktop\portfolio\raiotproj")
df = pd.read_csv("WHO-COVID-19-global-table-data.csv" ,  encoding="ISO-8859-1")

st.sidebar.header("Choose your filter: ")
region = st.sidebar.multiselect("Pick your Region", df["WHO Region"].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df["WHO Region"].isin(region)]

country = st.sidebar.multiselect("Pick the Countries", df2["Name"].unique() )
if not country:
    df3 = df2.copy()
else:
    df3 = df2[df2["Name"].isin(country)]
top_n = st.sidebar.slider("Select number of countries:", 5, 30, 10)

df.rename(columns={
        'Name': 'Countries',
       
    }, inplace=True)

# filter the data based on region and country
if not region and not country:
    filtered_df = df
elif region and not country:
    filtered_df = df[df["WHO Region"].isin(region)]
elif not region and country:
    filtered_df = df[df["Countries"].isin(country)]
else:
    filtered_df = df[(df["WHO Region"].isin(region)) & (df["Countries"].isin(country))]

filtered_df1 = filtered_df[filtered_df["Countries"] != "Global"]


top10 = filtered_df.sort_values(by='Cases - cumulative total', ascending=False).head(top_n)
pie1 = filtered_df1.sort_values(by='Cases - cumulative total', ascending=False).head(top_n)
top15 = filtered_df.sort_values(by='Deaths - cumulative total', ascending=False).head(top_n)

# Display basic info
st.subheader("📋 Dataset Overview")
st.dataframe( filtered_df)

# horizontal bar graph for cases
fig = px.bar(
    top10,
    x="Countries",
    y= 'Cases - cumulative total',
    color="Countries",
    title=f"Top {top_n} Countries by {'Cases - cumulative total'.capitalize()}",
    text='Cases - cumulative total',
)
st.plotly_chart(fig, use_container_width=True)

# horizontal bar graph for deaths
fig = px.bar(
    top15,
    x="Countries",
    y= 'Deaths - cumulative total',
    color="Countries",
    title=f"Top {top_n} Countries by {'Deaths - cumulative total'.capitalize()}",
    text='Deaths - cumulative total',
)
st.plotly_chart(fig, use_container_width=True)

# Pie Chart
st.subheader(f"Top {top_n} Countries by Total Cases (Pie Chart)")
pie_fig = px.pie(
    pie1,
    values='Cases - cumulative total',
    names="Countries",
    color='Countries',
    title=f"Distribution of Total Cases among Top {top_n} Countries",
)
st.plotly_chart(pie_fig, use_container_width=True)

# Scatter Plot: Cases vs Deaths
st.subheader("Scatter Plot: Total Cases vs Total Deaths")

scatter_fig = px.scatter(
    filtered_df,
    x='Cases - cumulative total',
    y='Deaths - cumulative total',
    color='WHO Region',
    hover_name='Countries',
    size='Cases - cumulative total',
    title="Cases vs Deaths by Country",
    size_max=40,
)

st.plotly_chart(scatter_fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("👩‍💻 *Built using Python, Streamlit, Matplotlib, and Seaborn*")
