fam = [1.73, 1.68, 1.71, 1.89]
for height in fam:
    print(height)
    # first iteration
    # height = 1.73
    # second iteration
    # height = 1.68

# Getting the index
for index, height in enumerate(fam):
    print("index " + str(index) + ": " + str(height))

# Loop over string
for c in "family":
    print(c.capitalize())
