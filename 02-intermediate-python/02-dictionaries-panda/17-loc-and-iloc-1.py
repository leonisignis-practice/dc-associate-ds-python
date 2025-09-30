# Import cars data
import pandas as pd

cars = pd.read_csv("cars.csv", index_col=0)

# Print out observation for Japan
print(cars.loc["JPN"])  # loc uses the label index
print(cars.iloc[2])  # iloc uses the integer index

# Print out observations for Australia and Egypt
print(cars.loc[["AUS", "EG"]])  # loc uses the label index
print(cars.iloc[[2, 6]])  # iloc uses the integer index
