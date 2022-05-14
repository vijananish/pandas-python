"""
This is about changing particular values in dataframe and removing duplicates
"""
import pandas as pd
data = pd.read_csv('data.csv')
print(data.head())

# Changing value using loc
print("----------------------")
print("Changing value using loc")
print("----------------------")
data.loc[1, "Pulse"] = 120
print(data.head())

# Changing value using iloc
print("----------------------")
print("Changing value using iloc")
print("----------------------")
data.loc[1, 1] = 120
print(data.head())

# drop duplicates
print("----------------------")
print("drop duplicates")
print("----------------------")
print("before duplicates shape: ", data.shape)
data.drop_duplicates(inplace=True)
print("after duplicates shape: ", data.shape)
