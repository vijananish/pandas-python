"""
This is about correlation in pandas
"""
import pandas as pd
data = pd.read_csv('data.csv')
print(data.corr())
