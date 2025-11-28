import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv(r"C:\Users\Admin\Downloads\WHO-COVID-19-global-table-data.csv")
df = pd.DataFrame(data)
df=df[['Name','WHO Region','Cases - cumulative total','Deaths - cumulative total']]
print(df.head())
print(data.head())


top10 = data.sort_values(by='Cases - cumulative total', ascending=False).head(10)
top15 = data.sort_values(by='Deaths - cumulative total', ascending=False).head(15)

# horizontal bar graph
sns.set(style="whitegrid")
plt.figure(figsize=(10,6), layout='constrained')
sns.set_style("darkgrid")
sns.barplot(x='Deaths - cumulative total', y='Name', data=top15, palette='viridis')
plt.title("Top 15 Countries with Highest COVID-19 Deaths")
plt.xlabel("Total Deaths in Millions")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# vertical bar graph
plt.figure(figsize=(14,6), layout='constrained')
plt.bar(top10['Name'], top10['Cases - cumulative total'])
plt.title("Top 10 Countries with Highest COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Total Cases in millions")
plt.show()

#line plot graph
plt.figure(figsize=(10,6))
sns.scatterplot(
    x='Cases - cumulative total',
    y='Deaths - cumulative total',
    data=top10,
    hue='Name',
    legend=True
)
plt.title("COVID-19: Total Cases vs Total Deaths (Top 10 Countries)")
plt.xlabel("Total Cases")
plt.ylabel("Total Deaths")
plt.tight_layout()
plt.show()

# pie chart
plt.figure(figsize=(8,8))
plt.pie(top10['Cases - cumulative total'], labels=top10['Name'], autopct='%1.1f%%')
plt.title("COVID-19 Case Distribution (Top 10 Countries)")
plt.legend(loc='upper right')
plt.show()





