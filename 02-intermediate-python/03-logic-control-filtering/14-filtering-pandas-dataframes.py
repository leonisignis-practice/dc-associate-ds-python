import pandas as pd
import os

print(os.getcwd())

brics = pd.read_csv(
    r"02-intermediate-python\03-logic-control-filtering\brics.csv", index_col=0
)
print(brics)

# Select countries with area over 8 million km2
# 1. Get area column
# 2. Do compararison on area column
# 3. Use result to select countries

# 1. Get area column
print(brics["area"])
print(brics.loc[:, "area"])
print(brics.iloc[:, 2])

# 2. Do compararison on area column
is_huge = brics["area"] > 8
print(brics["area"] > 8)

# 3. Use result to select countries
print(brics[is_huge])
print(brics[brics["area"] > 8])

# Keeping areas between 8 and 10 million km2
import numpy as np

between = np.logical_and(brics["area"] > 8, brics["area"] < 10)
print(between)
print(brics[between])
