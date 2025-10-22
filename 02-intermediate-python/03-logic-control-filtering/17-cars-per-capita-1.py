# Import cars data
import pandas as pd

cars = pd.read_csv(
    r"02-intermediate-python\03-logic-control-filtering\cars.csv", index_col=0
)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars["cars_per_cap"]
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)

print(cars[cars["cars_per_cap"] > 500])
