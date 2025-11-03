world = {"afgahnistan": 30.55, "albania": 2.77, "algeria": 39.21}

# error!
# for key, value in world:
# print(key + " -- " + str(value))

# works
for key, value in world.items():
    print(key + " -- " + str(value))
# algeria -- 39.21
# afghanistan -- 30.55
# albania -- 2.77
# dictionaries are unordered

for k, v in world.items():
    print(key + " -- " + str(value))

import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height**2
for val in bmi:
    print(val)

# 2d numpy array
meas = np.array([np_height, np_weight])
for val in meas:
    print(val)
# prints the entire array
# [1.73, 1.68, 1.71, 1.89, 1.79]

for val in np.nditer(meas):
    print(val)

# Recap
# Dictionary
#   for key, val in my_dict.items():
# NumPy array
#   for val in np.nditer(my_array):
