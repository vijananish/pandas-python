"""
Pandas Dataframe
"""
import pandas as pd
import numpy as np

# Creating dataframe from numpy array
print("-------------------------------------")
print("Creating dataframe from numpy array")
print("-------------------------------------")
np_data = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(pd.DataFrame(np_data))

# Creating dataframe from 1 series data
print("-------------------------------------")
print("Creating dataframe from 1 series data")
print("-------------------------------------")
series_data = pd.Series([1, 2, 3])
print(pd.DataFrame([series_data]))

# Creating dataframe from 2 series data
print("-------------------------------------")
print("Creating dataframe from 2 series data")
print("-------------------------------------")
series_data1 = pd.Series([1, 2, 3])
series_data2 = pd.Series([4, 5, 6])
print(pd.DataFrame([series_data1, series_data2]))

# Creating dataframe from dictionary
print("-------------------------------------")
print("Creating dataframe from dictionary")
print("-------------------------------------")
dict_data = {
  "A": [420, 380, 390],
  "B": [50, 40, 45]
}
print(pd.DataFrame(dict_data))
