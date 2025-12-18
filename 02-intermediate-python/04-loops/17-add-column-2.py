# Import cars data
import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "cars.csv")

cars = pd.read_csv(file_path)  # this keeps the country column as data
# cars = pd.read_csv(file_path, index_col=0)

# Code for loop that adds COUNTRY column
# for label, row in cars.iterrows():
#     cars.loc[label, "COUNTRY"] = row["country"].upper()

cars["COUNTRY"] = cars["country"].apply(str.upper)

# Print cars
print(cars)
