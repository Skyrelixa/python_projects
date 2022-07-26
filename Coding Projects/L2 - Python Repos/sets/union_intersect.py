# demonstrating union and intersection with sets

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# union combines elements from both sets without duplication
union = odds.union(evens)
print(union)

# intersection only takes elements found in both sets
intersect = odds.intersection(evens)
print(intersect)

# can experiment with the above using primes as well