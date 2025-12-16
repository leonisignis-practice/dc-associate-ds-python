# Import numpy as np
import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
np_height = np.array(height)

baseball = [[180, 78.4], [215, 102.7], [210, 98.5], [188, 75.2]]
np_baseball = np.array(baseball)

# For loop over np_height
for height in np_height:
    print(f"{height} inches")

# For loop over np_baseball
for item in np.nditer(np_baseball):
    print(item)
