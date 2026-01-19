from pathlib import Path

file = "homelessness.csv"
path = Path(__file__).resolve().parent / file
print(path)

# Import pandas using the alias pd
import pandas as pd

homelessness = pd.read_csv(path)

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)
