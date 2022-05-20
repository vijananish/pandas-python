# PANDAS QUESTIONS

This is a collection of exercises that have been collected in the pandas mailing list, on stack 
overflow
and in the pandas documentation. The goal of this collection is to offer a quick reference for both old
and new 
users but also to provide a set of exercises for those who teach.

If you find an error or think you've a better way to solve some of them, feel
free to open an issue.

#### 1. Import pandas under the alias pd.

#### 2. Print the version of pandas that has been imported.

#### 3. Print out all the version information of the libraries that are required by the pandas library.

#### 4. Create a DataFrame df from this dictionary data which has the index labels.
```
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
```
```
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
```
#### 5. Display a summary of the basic information about this DataFrame and its data (hint: there is a single method that can be called on the DataFrame).

#### 6. Return the first 3 rows of the DataFrame df.

#### 7. Select just the 'animal' and 'age' columns from the DataFrame df.

#### 8. Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].

#### 9. Select only the rows where the number of visits is greater than 3.

#### 10. Select the rows where the age is missing, i.e. it is NaN.

#### 11. Select the rows where the animal is a cat and the age is less than 3.

#### 12. Select the rows the age is between 2 and 4 (inclusive).

#### 13. Change the age in row 'f' to 1.5.

#### 14. Calculate the sum of all visits in df (i.e. the total number of visits).

#### 15. Calculate the mean age for each different animal in df.

#### 16. Append a new row 'k' to df with your choice of values for each column. Then delete that row to return the original DataFrame.

#### 17. Count the number of each type of animal in df.

#### 18. Sort df first by the values in the 'age' in decending order, then by the value in the 'visits' column in ascending order (so row i should be first, and row d should be last).

#### 19. The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 'yes' should be True and 'no' should be False.

#### 20. In the 'animal' column, change the 'snake' entries to 'python'.

#### 21. For each animal type and each number of visits, find the mean age. In other words, each row is an animal, each column is a number of visits and the values are the mean ages (hint: use a pivot table).

#### 22. You have a DataFrame df with a column 'A' of integers. For example:
```df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})```
How do you filter out rows which contain the same integer as the row immediately above?
You should be left with a column containing the following values:
```1, 2, 3, 4, 5, 6, 7```

#### 23. Given a DataFrame of random numeric values:
```df = pd.DataFrame(np.random.random(size=(5, 3))) # this is a 5x3 DataFrame of float values```
how do you subtract the row mean from each element in the row?

#### 24. Suppose you have DataFrame with 10 columns of real numbers, for example:
```df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))```
Which column of numbers has the smallest sum? Return that column's label.

#### 25. How do you count how many unique rows a DataFrame has (i.e. ignore all rows that are duplicates)?

#### 26. In the cell below, you have a DataFrame df that consists of 10 columns of floating-point numbers. Exactly 5 entries in each row are NaN values. For each row of the DataFrame, find the column which contains the third NaN value. You should return a Series of column labels: e, c, d, h, d

#### 27. A DataFrame has a column of groups 'grps' and and column of integer values 'vals':
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
#### 28. The DataFrame df constructed below has two integer columns 'A' and 'B'. The values in 'A' are between 1 and 100 (inclusive). For each group of 10 consecutive integers in 'A' (i.e. (0, 10], (10, 20], ...), calculate the sum of the corresponding values in column 'B'.
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

#### 29. Consider a DataFrame df where there is an integer column 'X':
```
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
```
For each value, count the difference back to the previous zero (or the start of the Series, whichever is closer). These values should therefore be
```
[1, 2, 0, 1, 2, 3, 4, 0, 1, 2]
```
Make this a new column 'Y'.

#### 30. Consider the DataFrame constructed below which contains rows and columns of numerical data. Create a list of the column-row index locations of the 3 largest values in this DataFrame. In this case, the answer should be:
```
[(5, 7), (6, 4), (2, 5)]
```

#### 31. You are given the DataFrame below with a column of group IDs, 'grps', and a column of corresponding integer values, 'vals'.
```
df = pd.DataFrame({"vals": np.random.RandomState(31).randint(-30, 30, size=15), 
                   "grps": np.random.RandomState(31).choice(["A", "B"], 15)})
```
Create a new column 'patched_values' which contains the same values as the 'vals' any negative values in 'vals' with the group mean:
```
    vals grps  patched_vals
0    -12    A          13.6
1     -7    B          28.0
2    -14    A          13.6
3      4    A           4.0
4     -7    A          13.6
5     28    B          28.0
6     -2    A          13.6
7     -1    A          13.6
8      8    A           8.0
9     -2    B          28.0
10    28    A          28.0
11    12    A          12.0
12    16    A          16.0
13   -24    A          13.6
14   -12    A          13.6
```

#### 32. Implement a rolling mean over groups with window size 3, which ignores NaN value. For example consider the following DataFrame:
```
df = pd.DataFrame({'group': list('aabbabbbabab'),
                       'value': [1, 2, 3, np.nan, 2, 3, np.nan, 1, 7, 3, np.nan, 8]})
df
   group  value
0      a    1.0
1      a    2.0
2      b    3.0
3      b    NaN
4      a    2.0
5      b    3.0
6      b    NaN
7      b    1.0
8      a    7.0
9      b    3.0
10     a    NaN
11     b    8.0
The goal is to compute the Series:

0     1.000000
1     1.500000
2     3.000000
3     3.000000
4     1.666667
5     3.000000
6     3.000000
7     2.000000
8     3.666667
9     2.000000
10    4.500000
11    4.000000
E.g. the first window of size three for group 'b' has values 3.0, NaN and 3.0 and occurs at row index 5. Instead of being NaN the value in the new column at this row index should be 3.0 (just the two non-NaN values are used to compute the mean (3+3)/2)
```

#### 33. Create a DatetimeIndex that contains each business day of 2015 and use it to index a Series of random numbers. Let's call this Series s.

#### 34. Find the sum of the values in s for every Wednesday.

#### 35. For each calendar month in s, find the mean of values.

#### 36. For each group of four consecutive calendar months in s, find the date on which the highest value occurred.

#### 37. Create a DateTimeIndex consisting of the third Thursday in each month for the years 2015 and 2016.

#### 38. Some values in the the FlightNumber column are missing (they are NaN). These numbers are meant to increase by 10 with each row so 10055 and 10075 need to be put in place. Modify df to fill in these missing numbers and make the column an integer column (instead of a float column).

#### 39. The From_To column would be better as two separate columns! Split each string on the underscore delimiter _ to give a new temporary DataFrame called 'temp' with the correct values. Assign the correct column names 'From' and 'To' to this temporary DataFrame.

#### 40. Notice how the capitalisation of the city names is all mixed up in this temporary DataFrame 'temp'. Standardise the strings so that only the first letter is uppercase (e.g. "londON" should become "London".)

#### 41. Delete the From_To column from 41. Delete the From_To column from df and attach the temporary DataFrame 'temp' from the previous questions.df and attach the temporary DataFrame from the previous questions.

#### 42. In the Airline column, you can see some extra puctuation and symbols have appeared around the airline names. Pull out just the airline name. E.g. '(British Airways. )' should become 'British Airways'.

#### 43. In the RecentDelays column, the values have been entered into the DataFrame as a list. We would like each first value in its own column, each second value in its own column, and so on. If there isn't an Nth value, the value should be NaN. Expand the Series of lists into a new DataFrame named 'delays', rename the columns 'delay_1', 'delay_2', etc. and replace the unwanted RecentDelays column in df with 'delays'.

#### 44. Given the lists letters = ['A', 'B', 'C'] and numbers = list(range(10)), construct a MultiIndex object from the product of the two lists. Use it to index a Series of random numbers. Call this Series s.

#### 45. Check the index of s is lexicographically sorted (this is a necessary proprty for indexing to work correctly with a MultiIndex).

#### 46. Select the labels 1, 3 and 6 from the second level of the MultiIndexed Series.

#### 47. Slice the Series s; slice up to label 'B' for the first level and from label 5 onwards for the second level.

#### 48. Sum the values in s for each label in the first level (you should have Series giving you a total for labels A, B and C).

#### 49. Suppose that sum() (and other methods) did not accept a level keyword argument. How else could you perform the equivalent of s.sum(level=1)?

#### 50. Exchange the levels of the MultiIndex so we have an index of the form (letters, numbers). Is this new Series properly lexsorted? If not, sort it.

#### 51. Let's suppose we're playing Minesweeper on a 5 by 4 grid, i.e.
```
X = 5
Y = 4
```
To begin, generate a DataFrame df with two columns, 'x' and 'y' containing every coordinate for this grid. That is, the DataFrame should start:
```
   x  y
0  0  0
1  0  1
2  0  2
```

X = 5
Y = 4

#### 52. For this DataFrame df, create a new column of zeros (safe) and ones (mine). The probability of a mine occuring at each location should be 0.4.

#### 3. Now create a new column for this DataFrame called 'adjacent'. This column should contain the number of mines found on adjacent squares in the grid.

(E.g. for the first row, which is the entry for the coordinate (0, 0), count how many mines are found on the coordinates (0, 1), (1, 0) and (1, 1).)

#### 54. For rows of the DataFrame that contain a mine, set the value in the 'adjacent' column to NaN.

#### 55. Finally, convert the DataFrame to grid of the adjacent mine counts: columns are the x coordinate, rows are the y coordinate.