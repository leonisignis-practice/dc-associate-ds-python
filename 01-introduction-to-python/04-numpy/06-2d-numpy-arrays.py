import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

print(type(np_height))
print(type(np_weight))
print(np_height.shape)  # (5,)
print(np_weight.shape)  # (5,)
print(np_height.ndim)  # 1
print(np_weight.ndim)  # 1
print(np_height.size)  # 5
print(np_weight.size)  # 5
print(np_height.dtype)  # float64
print(np_weight.dtype)  # float64
print(np_height.itemsize)  # 8
print(np_weight.itemsize)  # 8
print(np_height.nbytes)  # 40
print(np_weight.nbytes)  # 40

# 2D NumPy Arrays
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79], [65.4, 59.2, 63.6, 88.4, 68.7]])

print(np_2d)
print(type(np_2d))
print(np_2d.shape)  # (2, 5)
print(np_2d.ndim)  # 2
print(np_2d.size)  # 10
print(np_2d.dtype)  # float64
print(np_2d.itemsize)  # 8
print(np_2d.nbytes)  # 80

# In NumPy, arrays can only contain a single data type.
# If you try to create an array with mixed data types,
# NumPy will upcast the array to the most flexible data type
# that can accommodate all the values.
np_mixed = np.array([1.73, "1.68", 1.71, 1.89, 1.79])
print(np_mixed)
print(np_mixed.dtype)  # <U32

# Subsetting
print(np_2d[0][2])  # 1.71
print(np_2d[0, 2])  # 1.71

# array([[1.68, 1.71],
#        [59.2, 63.6]])
print(np_2d[:, 1:3])  # All rows, columns 1 and 2

print(np_2d[1, :])  # [65.4 59.2 63.6 88.4 68.7]
print(np_2d[0, :])  # [1.73 1.68 1.71 1.89 1.79]
