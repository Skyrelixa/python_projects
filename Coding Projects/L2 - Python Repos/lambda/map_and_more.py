# map(func, seq)

a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))

# using list comprehension syntax...
c = [x*2 for x in a]
print(c)

# filter function....  filter(func, seq)
# only prints even nums here
b = filter(lambda x: x%2==0, a)
print(list(b))

# using list comp...
c = [x for x in a if x%2 == 0]
print(c)

# reduce(func, seq)
from functools import reduce
a = [1, 2, 3, 4, 5, 6]
# reduce always has two args
prod = reduce(lambda x, y: x*y, a)

#printing the product of all nums, 1*2*3*4*5*6
print(prod)