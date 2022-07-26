mydict = {
    "name" : "Max",
    "age" : 28,
    "city" : "New York"
}

print(mydict)

# calling and printing the name in the dict
mydict2 = dict(name="Mary", age=27, city="Boston")
value = mydict["name"]
print(value)

# creating a new key for the dict
mydict["email"] = "max@xyz.com"
print(mydict)

# deleting from a dict
del mydict["name"]
print(mydict)

# popping from a dict
mydict.pop("age")
print(mydict)
mydict.popitem()
print(mydict)

# using if statement with dict
if "name" in mydict:
    print(mydict["name"])
else:
    print("Not there.")

# using for statements with dict
for key in mydict:                      # prints keys, can also use mydict.keys()
    print(key)

for value in mydict.values():           # prints values
    print(value)

for key, value in mydict.items():       # both
    print(key, value)

# copying a dictionary
mydict = {
    "name" : "Max",
    "age" : 28,
    "city" : "New York"
}

mydict_cpy = mydict.copy()              # copies dict without accidentally editing both
mydict_cpy = dict(mydict)               # copies dict without accidentally editing both


# UPDATE METHOD
dict1 = dict(name="Mary", age=28, city="Boston")
dict2 = dict(name="Maria", age=17, email="New York")

dict1.update(dict2)
print(dict1)

# creating a dictionary with a tuple. we can use tuples but not lists, because lists are mutable
mytuple = (8,7)
mydict = {mytuple: 15}
print(mydict)