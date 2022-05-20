# PANDAS

## INTRODUCTION
It is a powerful, flexible, easy to use open source data analysis and manipulation tool.
![alt text](https://miro.medium.com/max/1400/1*Dss7A8Z-M4x8LD9ccgw7pQ.png)

## DATA FOR PANDAS
In the data is mostly in tabular, database, json
1. Explore
2. Clean
3. Process


## READ, WRITE DATA
It supports many formats. Eg. (excel, csv, sql, json)
1. For read prefix = “read_*”
2. For write prefix = “to_*”


## CREATE PLOT
For plotting the data (scatter, lin, pie, etc) one can use the power of matplotlib, seaborn, plotly.


## USES
1. Reshape
2. Create new column
3. Calculate summary
4. Combine multiple table
5. Select subset


## LOC VS ILOC
1. Loc one needs to specify the name of the column and rows. Many operations can be performed on loc.
2. iLoc one needs to specify the index of the column and row.
![alt text](https://miro.medium.com/max/1400/1*dYtynwab99wnMqfgyPUd3w.png)

## DATA STRUCTURE
1. Series (1-D)
2. Dataframe (2-D)
3. Panel (3-D)
![alt text](https://techtipnow.in/wp-content/uploads/2021/05/panda-data-structure-chart.png)

## DROP ROWS/COLUMNS
On dropping rows, the value of the index will not adjust automatically. Therefore, use reset_index but will create a new column having old index values therefore drop=True in order not to make a column.
Make use of subset in order to drop “na” for a particular column.

## KEYWORDS
1. ```(inplace = True)``` : will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame
2. ```to_``` : prefix in order to convert type of data column to other type.
3. ```corr()``` : to find the correlation in the data.
4. Both isna() and isnull() functions are used to find the missing values in the pandas dataframe. isnull() and isna() literally does the same things. isnull() is just an alias of the isna() method as shown in pandas source code. Missing values are used to denote the values which are null or do not have any actual values.
5. ```df.replace```: in order to replace the particular value with another.
6. ```df.pivot_table()```: The levels in the pivot table will be stored in MultiIndex objects (hierarchical indexes) on the index and columns of the result DataFrame.