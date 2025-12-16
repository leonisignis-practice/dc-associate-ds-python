# Import cars data
import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "cars.csv")

cars = pd.read_csv(file_path, index_col=0)

# Adapt for loop
for lab, row in cars.iterrows():
    # print(lab + ": " + str(row["cars_per_cap"]))
    print(row.index)
