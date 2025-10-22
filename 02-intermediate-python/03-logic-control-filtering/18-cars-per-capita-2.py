# Import cars data
import pandas as pd

# Import numpy, you'll need this
import numpy as np

cars = pd.read_csv(
    r"02-intermediate-python\03-logic-control-filtering\cars.csv", index_col=0
)

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars["cars_per_cap"]
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)
