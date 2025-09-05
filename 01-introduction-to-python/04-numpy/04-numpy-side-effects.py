import numpy as np

np.array([True, 1, 2]) + np.array([3, 4, False])
# array([4, 5, 2])

np.array([4, 3, 0]) + np.array([0, 2, 2])
# array([4, 5, 2])

# When NumPy performs arithmetic operations on arrays with different data types,
# it converts the elements to a common, compatible type.
# In this case, since the arrays contain a mix of booleans and integers,
# NumPy promotes the boolean values to integers,
# where True is treated as 1 and False is treated as 0
