sister = "liz"  # Object type str

height = 1.73  # Object type float

fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]  # Object type list

fam.index("mom")  # Find index of "mom" using index method

fam.count(1.73)  # Count occurrences of 1.73 using count method

# Different data types have different methods
sister.upper()  # Convert string to uppercase
height.is_integer()  # Check if float is integer
fam.append("baby")  # Add new element to list

# In Python everything is an object
# Objects have methods associated with them and their type

# Some methods change the object they're call on
fam.append("me")
fam.append(1.79)
fam.remove("baby")  # Remove element from list

# Some methods don't change the object they're called on
sister.upper()
height.is_integer()
fam.count(1.73)
fam.index("mom")
