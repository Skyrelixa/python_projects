setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# difference returns the set with all elements from the first set that are NOT in the second set
# in other words, all the elements in setA not in setB

# you can also use setB.symmetric_difference(setA). This returns all values not common to both sets
diff = setA.difference(setB)
print(diff)
diff2 = setB.difference(setA)
print(diff2)

# you can overwrite sets, intersect sets, or add to sets by updating
# setA.update(setB)
# print(setA)

#setA.intersection_update(setB)
#print(setA)

#setA.difference_update(setB)
#print(setA)

setA.symmetric_difference_update(setB)
print(setA)