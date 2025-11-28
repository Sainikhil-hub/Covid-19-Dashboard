# covid_dashboard_app.py
# Interactive COVID-19 Dashboard using Streamlit + Matplotlib + Seaborn

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit page setup
st.set_page_config(page_title="COVID-19 Dashboard (WHO Data)", layout="wide")
st.title("🦠 COVID-19 Data Visualization Dashboard")
st.markdown("**Source:** WHO Global COVID-19 Dataset")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("WHO-COVID-19-global-table-data.csv")
    df.columns = [col.strip() for col in df.columns]
    df.rename(columns={
        'Name': 'Country',
        'WHO Region': 'Region',
        'Cases - cumulative total': 'Total_Cases',
        'Deaths - cumulative total': 'Total_Deaths',
        'Cases - newly reported in last 24 hours': 'New_Cases',
        'Deaths - newly reported in last 24 hours': 'New_Deaths'
    }, inplace=True)
    df.dropna(subset=['Total_Cases'], inplace=True)
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")
selected_region = st.sidebar.selectbox("Select WHO Region", ["All"] + sorted(df["Region"].dropna().unique().tolist()))
if selected_region != "All":
    df = df[df["Region"] == selected_region]

# Display basic info
st.subheader("📋 Dataset Overview")
st.dataframe(df.head(10))

# Summary statistics
st.markdown("### 📈 Summary Statistics")
st.write(df[['Total_Cases', 'Total_Deaths', 'New_Cases', 'New_Deaths']].describe())

# Visualization 1: Top 10 countries by total cases
st.markdown("### 🌍 Top 10 Countries by Total Cases")
top10_cases = df.sort_values(by='Total_Cases', ascending=False).head(10)
fig1, ax1 = plt.subplots(figsize=(10,6))
sns.barplot(x='Total_Cases', y='Country', data=top10_cases, palette='viridis', ax=ax1)
ax1.set_title("Top 10 Countries by Total COVID-19 Cases")
st.pyplot(fig1)

# Visualization 2: Top 10 countries by total deaths
st.markdown("### ⚰️ Top 10 Countries by Total Deaths")
top10_deaths = df.sort_values(by='Total_Deaths', ascending=False).head(10)
fig2, ax2 = plt.subplots(figsize=(10,6))
sns.barplot(x='Total_Deaths', y='Country', data=top10_deaths, palette='rocket', ax=ax2)
ax2.set_title("Top 10 Countries by Total COVID-19 Deaths")
st.pyplot(fig2)

# Visualization 3: Pie chart of total cases by region
st.markdown("### 🧭 Cases Distribution by WHO Region")
region_cases = df.groupby('Region')['Total_Cases'].sum().sort_values(ascending=False)
fig3, ax3 = plt.subplots(figsize=(7,7))
ax3.pie(region_cases, labels=region_cases.index, autopct='%1.1f%%', startangle=140)
ax3.set_title("COVID-19 Cases Distribution by WHO Region")
st.pyplot(fig3)

# Visualization 4: Scatter plot (Cases vs Deaths)
st.markdown("### 📊 Cases vs Deaths Scatter Plot")
fig4, ax4 = plt.subplots(figsize=(10,6))
sns.scatterplot(x='Total_Cases', y='Total_Deaths', hue='Region', data=df, s=80, ax=ax4)
ax4.set_title("Total Cases vs Total Deaths (by Country)")
ax4.set_xlabel("Total Cases")
ax4.set_ylabel("Total Deaths")
st.pyplot(fig4)

# Visualization 5: Correlation heatmap
st.markdown("### 🔥 Correlation Heatmap")
num_cols = ['Total_Cases', 'Total_Deaths', 'New_Cases', 'New_Deaths']
corr = df[num_cols].corr()
fig5, ax5 = plt.subplots(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax5)
ax5.set_title("Correlation between COVID-19 Metrics")
st.pyplot(fig5)

# Visualization 6: Top 10 countries by new cases
st.markdown("### 🚨 Top 10 Countries by New Cases (Last 24 Hours)")
top10_new_cases = df.sort_values(by='New_Cases', ascending=False).head(10)
fig6, ax6 = plt.subplots(figsize=(10,6))
sns.barplot(x='New_Cases', y='Country', data=top10_new_cases, palette='mako', ax=ax6)
ax6.set_title("Top 10 Countries by New Cases (Last 24 Hours)")
st.pyplot(fig6)

# Footer
st.markdown("---")
st.markdown("👩‍💻 *Built using Python, Streamlit, Matplotlib, and Seaborn*")
