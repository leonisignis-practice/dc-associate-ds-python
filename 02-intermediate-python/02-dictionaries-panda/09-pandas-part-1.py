dict = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasília", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98],  # in millions
}

import pandas as pd

brics = pd.DataFrame(dict)
print(brics)

# keys (column labels)
# Values (data, column by column)
print(brics.keys())
print(brics.values)
print(brics.index)
print(brics.shape)  # (rows, columns)
print(brics.dtypes)
print(brics.describe())  # summary statistics for numerical columns
print(brics.info())  # concise summary of the DataFrame
print(brics.head())  # first 5 rows
print(brics.tail(2))  # last 2 rows

brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

brics = pd.read_csv("brics.csv")
print(brics)
#         country    capital    area  population
# 0        Brazil   Brasília   8.516      200.40
# 1        Russia     Moscow  17.100      143.50

brics = pd.read_csv("brics.csv", index_col=0)
print(brics)
#          country    capital    area  population
# BR        Brazil   Brasília   8.516      200.40
# RU        Russia     Moscow  17.100      143.50
