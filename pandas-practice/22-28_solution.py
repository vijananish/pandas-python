"""
This contains solution from 22-28
"""
import numpy as np
import pandas as pd

"""
22. You have a DataFrame df with a column 'A' of integers. For example:
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
How do you filter out rows which contain the same integer as the row immediately above?
You should be left with a column containing the following values:
```1, 2, 3, 4, 5, 6, 7```
"""
print("--------------------------------------")
print("22. You have a DataFrame df with a column 'A' of integers.")
print("--------------------------------------")
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
print(df.drop_duplicates().reset_index(drop=True))

"""
23. Given a DataFrame of random numeric values:
```df = pd.DataFrame(np.random.random(size=(5, 3))) # this is a 5x3 DataFrame of float values```
how do you subtract the row mean from each element in the row?
"""
print("--------------------------------------")
print("23. Given a DataFrame of random numeric")
print("--------------------------------------")
df = pd.DataFrame(np.random.random(size=(5, 3)))
print(df)
print(df.sub(df.mean(axis=1), axis=0))


"""
24. Suppose you have DataFrame with 10 columns of real numbers, for example:
```df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))```
Which column of numbers has the smallest sum? Return that column's label.
"""
print("--------------------------------------")
print("24. Suppose you have DataFrame with 10 columns of real numbers")
print("--------------------------------------")
df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
print(df.columns[df.sum(axis=1).argmax()])


# 25. How do you count how many unique rows a DataFrame has (i.e. ignore all rows that are duplicates)?
print("--------------------------------------")
print("25. How do you count how many unique rows a DataFrame has (i.e. ignore all rows that are duplicates)?")
print("--------------------------------------")
print(len(df.drop_duplicates(keep=False)))


# 26. In the cell below, you have a DataFrame df that consists of 10 columns of floating-point numbers.
# Exactly 5 entries in each row are NaN values. For each row of the DataFrame,
# find the column which contains the third NaN value. You should return a Series of column labels: e, c, d, h, d
# method that can be called on the DataFrame).
print("--------------------------------------")
print("26. In the cell below, you have a DataFrame df that consists of 10 columns of floating-point numbers. "
      "Exactly 5 entries in each row are NaN values. For each row of the DataFrame, "
      "find the column which contains the third NaN value. You should return a Series of column labels: e, c, d, h, d")
print("--------------------------------------")
print(df.info())


"""
27. A DataFrame has a column of groups 'grps' and and column of integer values 'vals':
```
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 
                   'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
```                   
For each group, find the sum of the three greatest values. You should end up with the answer as follows:
```
grps
a    409
b    156
c    345
```
"""
print("--------------------------------------")
print("27. A DataFrame has a column of groups 'grps' and and column of integer values 'vals'")
print("--------------------------------------")
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
                   'vals': [12, 345, 3, 1, 45, 14, 4, 52, 54, 23, 235, 21, 57, 3, 87]})
print(df.groupby("grps")['vals'].nlargest(3).sum(level=0))

"""
28. The DataFrame df constructed below has two integer columns 'A' and 'B'. The values in 'A' are between 
1 and 100 (inclusive). For each group of 10 consecutive integers in 'A' (i.e. (0, 10], (10, 20], ...), 
calculate the sum of the corresponding values in column 'B'.
The answer should be a Series as follows:
```
A
(0, 10]      635
(10, 20]     360
(20, 30]     315
(30, 40]     306
(40, 50]     750
(50, 60]     284
(60, 70]     424
(70, 80]     526
(80, 90]     835
(90, 100]    852
```
"""
df = pd.DataFrame(np.random.randint(1, 101, size=(100, 2)), columns=["A", "B"])
print(df.groupby(pd.cut(df["A"], bins=range(0, 101, 10)))["B"].sum())