# changing list elements
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

# dad shrank a bit
fam[7] = 1.79
print(fam)

# changing a set of elements
fam[0:2] = ["lisa", 1.74]
print(fam)

# adding and removing elements
fam = fam + ["me", 1.78]
print(fam)

# deleting elements
del fam[2]
print(fam)
del fam[2:5]
print(fam)

# behind the scenes (1)
x = ["a", "b", "c"]
y = x
y[1] = "z"
print(x)
print(y)

# behind the scenes (2)
x = ["a", "b", "c"]
y = list(x)
y = x[:]
y[1] = "z"
print(x)
print(y)
