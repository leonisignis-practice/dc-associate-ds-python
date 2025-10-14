# and
print(True and True)
print(False and True)
print(True and False)
print(False and False)

x = 12
print(x > 5 and x < 15)

# or
print(True or True)
print(False or True)
print(True or False)
print(False or False)

y = 5
print(y < 7 or y > 13)

# not
print(not True)
print(not False)

# numpy
import numpy as np

bmi = np.array([21.852, 20.975, 21.75, 24.747, 21.441])
print(bmi > 21)
print(bmi < 22)
# print(bmi > 21 and bmi < 22) # Error

print(np.logical_and(bmi > 21, bmi < 22))

print(bmi[np.logical_and(bmi > 21, bmi < 22)])
