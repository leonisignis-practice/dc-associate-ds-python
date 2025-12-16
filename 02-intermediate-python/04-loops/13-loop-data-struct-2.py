import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "brics.csv")

brics = pd.read_csv(file_path, index_col=0)

# This will print the labels only
for val in brics:
    print(val)

# In pandas we need to specify we want to iterate over the rows
for label, row in brics.iterrows():
    print(label)
    print(row)

# Printing only the capital
for label, row in brics.iterrows():
    print(f"{label}: {row['capital']}")

# Adding a column (Inefficient)
for label, row in brics.iterrows():
    # Creating Series on every iteration
    brics.loc[label, "name_length"] = len(row["country"])
print(brics)

# Using apply() to do the above more efficiently (vectorized operation)
brics = pd.read_csv(file_path, index_col=0)
brics["name_length"] = brics["country"].apply(len)
print(brics)
