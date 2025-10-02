import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height**2
print(bmi)

print(bmi > 23)  # Greater than 23
print(type(bmi > 23))  # The type is a numpy array
print(np.any(bmi > 23))  # Are there any values greater than 23
print(np.all(bmi < 23))  # Are all values less than 23

print([bmi < 23])  # Less than 23
print(type([bmi < 23]))  # The type is a list
print(bmi[bmi < 23])  # Filtered array of values less than 23

# Numeric comparisons
print(2 < 3)
print(2 == 3)
print(2 != 3)
print(2 <= 3)
print(3 <= 3)

x = 2
y = 3
print(x < y)  # True

print("car" < "chris")  # True, because 'a' comes before 'h' in the alphabet
# print(3 < 'chris') # Error: cannot compare different data types
print(3 < 4.1)  # True, int and float can be compared
print(3 == 3.0)  # True, int and float can be compared
