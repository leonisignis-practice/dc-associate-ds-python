import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:, 0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))

# Print out the standard deviation of np_height_in
print(np.std(np_height_in))

# Print out the correlation between np_height_in and np_weight_lb
np_weight_lb = np_baseball[:, 1]
print(np.corrcoef(np_height_in, np_weight_lb))
