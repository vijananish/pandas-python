"""
This is about cleaning empty cells in dataframe
"""
import pandas as pd
data = pd.read_csv("data.csv")
print(data.shape)


# dropping na rows
print("-----------------------------------")
print("dropping na rows")
print("-----------------------------------")
data_dr = data.dropna()
print(data_dr.shape)

# dropping rows that are na in particular column
print("-----------------------------------")
print("dropping na rows")
print("-----------------------------------")
data_drc = data.dropna(subset=['Calories'])
print(data_drc.shape)

# fill na mean
print("-----------------------------------")
print("fill na mean")
print("-----------------------------------")
data_mr = data["Calories"].fillna(data["Calories"].mean())
print("mean of calories: ", data["Calories"].mean())
print(data_mr.info())

# fill na median
print("-----------------------------------")
print("fill na median")
print("-----------------------------------")
data_mer = data["Calories"].fillna(data["Calories"].median())
print("median of calories: ", data["Calories"].median())
print(data_mr.info())

# fill na mode
print("-----------------------------------")
print("fill na mode")
print("-----------------------------------")
data_mor = data["Calories"].fillna(data["Calories"].mode())
print("mode of calories: ", data["Calories"].mode())
print(data_mr.info())
