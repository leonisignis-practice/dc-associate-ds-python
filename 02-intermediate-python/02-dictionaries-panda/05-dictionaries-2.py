world = {"afghanistan": 30.55, "albania": 2.77, "algeria": 39.21}
print(world["albania"])

# only one key 'albania' is allowed
# the last assignment to 'albania' will be kept
world = {"afghanistan": 30.55, "albania": 2.77, "algeria": 39.21, "albania": 2.81}
print(world)

# The keys must be immutable types
# The values can be of any type
dict1 = {0: "hello", True: "dear", "two": "world"}
print(dict1)  # {0: 'hello', True: 'dear', 'two': 'world'}
# dict2 = {["just", "to", "test"]: "value"}  # TypeError: unhashable type: 'list'
dict3 = {("just", "to", "test"): "value"}  # Works fine
print(dict3)  # {('just', 'to', 'test'): 'value'}

# Principality of Sealand
world["sealand"] = 0.000027
print(world)

print("sealand" in world)  # True
print("india" in world)  # False
print("india" not in world)  # True

# Update the value for key 'sealand'
world["sealand"] = 0.000028
print(world)

# delete the key 'sealand'
del world["sealand"]
print(world)
