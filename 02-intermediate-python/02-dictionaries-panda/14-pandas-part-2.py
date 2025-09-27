import pandas as pd

# brics = pd.read_csv("path/to/brics.csv", index_col=0)
dict = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasília", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98],  # in millions
}

brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

# only select the country column
print(brics["country"])
print(type(brics["country"]))  # <class 'pandas.core.series.Series'>
# A panda series is a one-dimensional array with axis labels (like a dict)ionary)
# A panda dataframe is a two-dimensional array with axis labels (like a spreadsheet or a SQL table)

type(brics[["country"]])  # <class 'pandas.core.frame.DataFrame'>
# double brackets returns a dataframe instead of a series
print(brics[["country", "capital"]])
# print(brics["country", "capital"])  # KeyError: ('country', 'capital')
# multiple columns
print(brics[0:3])  # first three rows
print(brics[brics["area"] > 8])  # rows where area is greater than 8
print(
    brics[brics["area"] > 8][["country", "capital"]]
)  # rows where area is greater than 8, only country and capital columns

# row access
print(brics[1:4])  # rows at index positions 1, 2, and 3
# print(brics[1, 3])  # Error, pandas does not support this

# In numpy we use my_array[row, column]
# In pandas we use my_dataframe.loc[row_label, column_label]
# or my_dataframe.iloc[row_index, column_index]
# .loc is label-based, which means that you have to specify rows and columns based on
print(brics.loc["RU"])  # row with index label 'RU'. This is a panda series
print(brics.loc[["RU"]])  # row with index label 'RU'. This is a panda dataframe

# rows with index labels 'RU', 'IN', and 'CH', only country and capital columns
print(brics.loc[["RU", "IN", "CH"], ["country", "capital"]])

# all rows, only country and capital columns
print(brics.loc[:, ["country", "capital"]])

# using iloc
print(brics.loc["RU"])  # row with index label 'RU'
print(brics.iloc[1])  # row at index position 1, as a series
print(brics.iloc[[1]])  # row at index position 1, as a dataframe

print(brics.loc[["RU", "IN", "CH"]])  # rows with index labels 'RU', 'IN', and 'CH'
print(brics.iloc[[1, 2, 3]])  # rows at index positions 1, 2, and 3

# rows with index labels 'RU', 'IN', and 'CH', only country and capital columns
print(brics.loc[["RU", "IN", "CH"], ["country", "capital"]])
# rows at index positions 1, 2, and 3, only country and capital columns
print(brics.iloc[[1, 2, 3], [0, 1]])

# all rows, only country and capital columns
print(brics.loc[:, ["country", "capital"]])
print(brics.iloc[:, [0, 1]])
# all rows, all columns
print(brics.loc[:, :])
print(brics.iloc[:, :])
print(brics)  # same as brics.loc[:, :]
