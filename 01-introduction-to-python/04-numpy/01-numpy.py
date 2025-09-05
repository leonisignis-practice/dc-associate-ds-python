height = [1.73, 1.68, 1.71, 1.89, 1.79]
print(height)

weight = [65.4, 59.2, 63.6, 88.4, 68.7]
print(weight)

# The following lines will raise an error
# because Python doesn't know how to work with arrays directly
# weight / height**2
# bmi = weight / height**2

import numpy as np

np_height = np.array(height)
print(np_height)

np_weight = np.array(weight)
print(np_weight)

bmi = np_weight / np_height**2
print(bmi)

# remarks
python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])

print(python_list + python_list)  # append / repeat 2 times
print(numpy_array + numpy_array)  # element-wise addition
print(python_list * 3)  # repeat 3 times
print(numpy_array * 3)  # element-wise multiplication

# different types, different behaviors

# numpy subsetting
print(bmi[1])
print(bmi > 23)

# using the mask
print(bmi[bmi > 23])
