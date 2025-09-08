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
