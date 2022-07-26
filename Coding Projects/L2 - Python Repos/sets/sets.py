# sets are unordered, mutable, and hold NO duplicates
# unlike lists, which can hold duplicates

myset = {1, 2, 3, 1, 2}             # result does not store the extra 1 and 2
print(myset)

myset = set([1, 2, 3])
print(myset)

# order of hello will be randomized. parses the letters
myset = set("Hello")
print(myset)

# an empty set will be recognized as a dict with just brackets
myset = {}
print(type(myset))
myset = set()                       # solution
print(type(myset))  

# adding and removing elements to a set, then clearing. 
# better to use .discard() in place of .remove() if you want no exception errors
# in the case a value is not found in the set
myset.add(1)
myset.add(2)
myset.add(3)
myset.remove(3)

print(myset)

myset.clear()
print(myset)

# popping
myset = {1, 2, 3}
print(myset.pop())

# iterations with sets, and if's with sets
for i in myset:
    print(i)

if 2 in myset:
    print("Yes")
else:
    print("No")