# Import cars data
import pandas as pd

cars = pd.read_csv(
    r"02-intermediate-python\03-logic-control-filtering\cars.csv", index_col=0
)

# Convert code to a one-liner
print(cars[cars["drives_right"]])
