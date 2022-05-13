"""
Pandas Series
"""
import pandas as pd
data = [1, 2, 3]
series = pd.Series(data, index=["a", "b", "c"])
print(series)
