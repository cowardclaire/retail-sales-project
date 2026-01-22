import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   
import sklearn as sk

#checking data loaded correctly, showing first few rows and info

df = pd.read_csv("Online Retail.csv")
print(df.head())
print(df.info())

#checking for missing values
print(df.isnull().sum())

#clean data, and creating a function 

def clean_data(df):
    df['Description'] = df['Description'].fillna('No Description')
    return df

df = clean_data(df)
print(df.isnull().sum())