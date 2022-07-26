from itertools import product

a = [1, 2]
b = [3]

p = product(a, b, repeat = 2)
print(list(p))