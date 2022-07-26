# you can check whether setA is subset of setB 
# in other words, is setB a superset?

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}

print(setB.issubset(setA))

# you can also check whether setA is a superset of setB
# in other words, is setB a subset?

print(setB.issuperset(setA))

# checking if sets have no common elements
print(setB.isdisjoint(setC))