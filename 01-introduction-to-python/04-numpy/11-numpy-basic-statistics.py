import numpy as np

# Sample data: Each row represents [height (m), weight (kg)]
np_city = np.array(
    [
        [1.64, 71.78],
        [1.37, 63.35],
        [1.6, 55.09],
        [2.04, 74.85],
        [2.04, 68.72],
        [2.01, 73.57],
    ]
)
print("City Data:\n", np_city)

# Building from random distribution
height = np.round(np.random.normal(1.75, 0.2, 5000), 2)  # mean=1.75m, std=0.2m
weight = np.round(np.random.normal(60.32, 15, 5000), 2)  # mean=70kg, std=15kg
np_city = np.column_stack((height, weight))
print("\nGenerated City Data (first 5 rows):\n", np_city[:5])

# Mean
mean_height = np.mean(np_city[:, 0])
print("Mean Height:", mean_height)

# Median
median_weight = np.median(np_city[:, 1])
print("Median Weight:", median_weight)

# Correlation Coefficient
correlation_matrix = np.corrcoef(np_city[:, 0], np_city[:, 1])
correlation = correlation_matrix[0, 1]
print("Correlation between Height and Weight:", correlation)

# Standard Deviation
std_dev_height = np.std(np_city[:, 0])
print("Standard Deviation of Height:", std_dev_height)
std_dev_weight = np.std(np_city[:, 1])
print("Standard Deviation of Weight:", std_dev_weight)
