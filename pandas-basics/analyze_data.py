"""Basic Analysis of Data"""
import pandas as pd
data = pd.read_csv("data.csv")

# Head
print("--------------------------------")
print("Data Head")
print("--------------------------------")
print(data.head())

# Tail
print("--------------------------------")
print("Data Tail")
print("--------------------------------")
print(data.tail())

# Describe
print("--------------------------------")
print("Data Describe")
print("--------------------------------")
print(print(data.describe()))

# Info
print("--------------------------------")
print("Data Info")
print("--------------------------------")
print(data.info())

# Null Count
print("--------------------------------")
print("Null Count")
print("--------------------------------")
print(data.isnull().value_counts())
