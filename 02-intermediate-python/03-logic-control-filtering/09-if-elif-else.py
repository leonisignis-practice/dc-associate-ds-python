# if statement
z = 4
if z % 2 == 0:
    print("z is even")

# if statement with multiple lines
z = 4
if z % 2 == 0:
    print("checking " + str(z))
    print("z is even")

# else statement
z = 5
if z % 2 == 0:
    print("z is even")
else:
    print("z is odd")

# multiple else statements, elif
z = 3
if z % 2 == 0:
    print("z is divisible by 2")
elif z % 3 == 0:
    print("z is divisible by 3")
else:
    print("z is neighter divisible by 2 nor by 3")
