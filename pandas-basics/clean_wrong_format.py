"""
This is about cleaning wrong format
"""
import pandas as pd
df = pd.read_csv('data.csv')
print("----------------------")
print("format before")
print("----------------------")
print(df.info())
df['Duration'] = pd.to_datetime(df['Duration'])
print("----------------------")
print("format after")
print("----------------------")
print(df.info())
