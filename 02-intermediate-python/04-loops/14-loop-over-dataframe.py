import os

# Import cars data
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "cars.csv")

cars = pd.read_csv(file_path, index_col=0)

# Iterate over rows of cars
for label, car in cars.iterrows():
    print(label)
    print(car)
