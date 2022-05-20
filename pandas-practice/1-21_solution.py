"""
This contains solution from 1-21
"""
import numpy as np

# 1. Import pandas under the alias pd.
print("--------------------------------------")
print("1. Import pandas under the alias pd.")
print("--------------------------------------")
import pandas as pd


# 2. Print the version of pandas that has been imported.
print("--------------------------------------")
print("2. Print the version of pandas that has been imported.")
print("--------------------------------------")
print(pd.__version__)

# 3. Print out all the version information of the libraries that are required by the pandas library.
print("--------------------------------------")
print("3. Print out all the version information of the libraries that are required by the pandas library.")
print("--------------------------------------")
print(pd.show_versions())

# 4. Create a DataFrame df from this dictionary data which has the index labels.
"""
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
"""
print("--------------------------------------")
print("4. Create a DataFrame df from this dictionary data which has the index labels.")
print("--------------------------------------")
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
print(df)

# 5. Display a summary of the basic information about this DataFrame and its data (hint: there is a single
# method that can be called on the DataFrame).
print("--------------------------------------")
print("5. Display a summary of the basic information about this DataFrame and its data (hint: there is a single "
      "method that can be called on the DataFrame).")
print("--------------------------------------")
print(df.info())

# 6. Return the first 3 rows of the DataFrame df.
print("--------------------------------------")
print("6. Return the first 3 rows of the DataFrame df.")
print("--------------------------------------")
print(df[:3])

# 7. Select just the 'animal' and 'age' columns from the DataFrame df.
print("--------------------------------------")
print("7. Select just the 'animal' and 'age' columns from the DataFrame df.")
print("--------------------------------------")
print(df[["age", "animal"]])

# 8. Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].
print("--------------------------------------")
print("8. Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].")
print("--------------------------------------")
print(df[["age", "animal"]].iloc[[3, 4, 8]])

# 9. Select only the rows where the number of visits is greater than 3.
print("--------------------------------------")
print("9. Select only the rows where the number of visits is greater than 3.")
print("--------------------------------------")
print(df[df["visits"]>3])

# 10. Select the rows where the age is missing, i.e. it is NaN.
print("--------------------------------------")
print("10. Select the rows where the age is missing, i.e. it is NaN.")
print("--------------------------------------")
print(df[df["age"].isnull()])

# 11. Select the rows where the animal is a cat and the age is less than 3.
print("--------------------------------------")
print("11. Select the rows where the animal is a cat and the age is less than 3.")
print("--------------------------------------")
print(df[(df["animal"] == "cat") & (df["age"] < 3)])

# 12. Select the rows the age is between 2 and 4 (inclusive).
print("--------------------------------------")
print("12. Select the rows the age is between 2 and 4 (inclusive).")
print("--------------------------------------")
print(df[(df["age"] > 2) & (df["age"] < 4)])

# 13. Change the age in row 'f' to 1.5.
print("--------------------------------------")
print("13. Change the age in row 'f' to 1.5.")
print("--------------------------------------")
df.loc[['f'], ["age"]] = 1.5
print(df)

# 14. Calculate the sum of all visits in df (i.e. the total number of visits).
print("--------------------------------------")
print("14. Calculate the sum of all visits in df (i.e. the total number of visits).")
print("--------------------------------------")
print(df["visits"].sum())

# 15. Calculate the mean age for each different animal in df.
print("--------------------------------------")
print("15. Calculate the mean age for each different animal in df.")
print("--------------------------------------")
print(df.groupby("animal")["age"].mean())


# 16. Append a new row 'k' to df with your choice of values for each column.
# Then delete that row to return the original DataFrame.
print("--------------------------------------")
print("16. Append a new row 'k' to df with your choice of values for each column. "
      "Then delete that row to return the original DataFrame.")
print("--------------------------------------")
df.loc[len(df.index)] = "tiger", 2, 1, "yes"

print(df)

# 17. Count the number of each type of animal in df.
print("--------------------------------------")
print("17. Count the number of each type of animal in df.")
print("--------------------------------------")
print(df["animal"].value_counts())

# 18. Sort df first by the values in the 'age' in descending order, then by the value in the 'visits' column in
# ascending order (so row i should be first, and row d should be last).
print("--------------------------------------")
print("18. Sort df first by the values in the 'age' in descending order, then by the value in the 'visits' column "
      "in ascending order (so row i should be first, and row d should be last).")
print("--------------------------------------")
print(df.sort_values(by="age", axis=0, ascending=False))

# 19. The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values:
# 'yes' should be True and 'no' should be False.
print("--------------------------------------")
print("19. The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean "
      "values: 'yes' should be True and 'no' should be False.")
print("--------------------------------------")
df["priority"].replace("no", False, inplace=True)
df["priority"].replace("yes", True, inplace=True)
print(df)

# 20. In the 'animal' column, change the 'snake' entries to 'python'.
print("--------------------------------------")
print("20. In the 'animal' column, change the 'snake' entries to 'python'.")
print("--------------------------------------")
df["animal"].replace("snake", "python", inplace=True)
print(df)

# 21. For each animal type and each number of visits, find the mean age. In other words, each row is an animal,
# each column is a number of visits and the values are the mean ages (hint: use a pivot table).
print("--------------------------------------")
print("21. For each animal type and each number of visits, find the mean age. In other words, each row is an animal, "
      "each column is a number of visits and the values are the mean ages (hint: use a pivot table).")
print("--------------------------------------")
print(df.pivot_table(index="animal", columns="visits", aggfunc=np.mean))
