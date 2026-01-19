from pathlib import Path

file = "homelessness.csv"
path = Path(__file__).resolve().parent / file
print(path)

# Import pandas using the alias pd
import pandas as pd

homelessness = pd.read_csv(path)

# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())
