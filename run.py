import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   
import sklearn as sk

#checking data loaded correctly, showing first few rows and info

df = pd.read_csv("Data/Online Retail.csv")
print(df.head())
print(df.info())

#checking for missing values
print(df.isnull().sum())

#clean data, and creating a function 

def clean_data(df):

    #fill in no description for missing values
    df['Description'] = df['Description'].fillna('No Description')

    #converting the data types
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['CustomerID'] = df['CustomerID'].astype('Int64')

    return df

df = clean_data(df)
print(df.isnull().sum())

#create new variable
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
print(df.head())

#store cleaned data
df.to_csv("Cleaned_Online_Retail.csv", index=False)

#visualising data

#graph showing total revenue over time
daily = df.groupby(df['InvoiceDate'].dt.date)['TotalPrice'].sum()

plt.figure(figsize=(12,5))
plt.plot(daily)
plt.title('Daily Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue')
#plt.show()

#bar chart showing top 10 products by revenue
top_products = df.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(10)  
plt.figure(figsize=(12,5))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title('Top 10 Products by Revenue') 
plt.xlabel('Revenue')
plt.ylabel('Product Description')   
#plt.show()

#pie chart showing revenue distribution by country
country_revenue = df.groupby('Country')['TotalPrice'].sum()
plt.figure(figsize=(8,8))   
plt.pie(country_revenue, labels=country_revenue.index, startangle=140)
plt.title('Revenue Distribution by Country')    
#plt.show()

#reducing country names

country_list = df["Country"].dropna().drop_duplicates().sort_values()
print(country_list)

# 1. Compute total revenue per country
country_revenue = (
    df.groupby("Country")["TotalPrice"]
      .sum()
      .sort_values(ascending=False)
)

# 2. Identify the top 10 countries
top10 = country_revenue.head(10).index

# 3. Create a new grouped country column
df["Country_Grouped"] = df["Country"].where(df["Country"].isin(top10), "Other")

# Optional: see the grouped revenue
summary = (
    df.groupby("Country_Grouped")["TotalPrice"]
      .sum()
      .sort_values(ascending=False)
)

print(summary)

#pie chart showing revenue distribution by country grouped to 10 and other

grouped_revenue = df.groupby('Country_Grouped')['TotalPrice'].sum()
plt.figure(figsize=(8,8))   
plt.pie(grouped_revenue, labels=grouped_revenue.index, startangle=140)          
plt.title('Revenue Distribution by Country (Grouped)')
plt.show()