# Covid-19 Dashboard using Matplotlib & Seaborn
# Author: [Your Name]
# Topic: Data Visualization with Matplotlib & Seaborn

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------
# Step 1: Fetch data from API
# --------------------------
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)
data = response.json()

# --------------------------
# Step 2: Convert to DataFrame
# --------------------------
df = pd.DataFrame(data)

# Select important columns
df = df[['country', 'cases', 'todayCases', 'deaths', 'todayDeaths', 'recovered', 'active', 'population']]

# Sort countries by total cases (top 10)
top10 = df.sort_values(by='cases', ascending=False).head(10)

# --------------------------
# Step 3: Data Visualization
# --------------------------

# Set Seaborn theme
sns.set(style="whitegrid")

# --- Bar Chart: Top 10 countries by total cases ---
plt.figure(figsize=(10,6))
sns.barplot(x='cases', y='country', data=top10, palette='Reds_r')
plt.title("Top 10 Countries with Highest COVID-19 Cases")
plt.xlabel("Total Cases")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# --- Line Plot: Cases vs Deaths ---
plt.figure(figsize=(10,6))
sns.scatterplot(x='cases', y='deaths', data=df, hue='country', legend=False)
plt.title("COVID-19: Total Cases vs Total Deaths (All Countries)")
plt.xlabel("Total Cases")
plt.ylabel("Total Deaths")
plt.tight_layout()
plt.show()

# --- Heatmap: Correlation between Variables ---
plt.figure(figsize=(8,6))
corr = df[['cases', 'deaths', 'recovered', 'active', 'population']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap of COVID-19 Parameters")
plt.tight_layout()
plt.show()

# --------------------------
# Step 4: Summary
# --------------------------
print("\nSummary of Top 10 Affected Countries:")
print(top10[['country', 'cases', 'deaths', 'recovered', 'active']])
