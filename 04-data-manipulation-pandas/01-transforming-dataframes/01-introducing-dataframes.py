import os

dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(dir, "dogs.csv")

import pandas as pd

dogs_df = pd.read_csv(file)

print(dogs_df)
# First 5 rows
print(dogs_df.head())
# Names of columns, datatypes and if they have missing values
print(dogs_df.info())
# Number of rows, Number of Columns
print(dogs_df.shape)
# Summary statistics
print(dogs_df.describe())  # count is non-missing values
# 2D numpy array
print(dogs_df.values)
# Labels for columns
print(dogs_df.columns)
# Labels for rows
print(dogs_df.index)
