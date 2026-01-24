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

