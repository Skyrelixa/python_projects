# sets a default if the key is not yet set
from collections import defaultdict

d = defaultdict(int)        # can also use float, list, and more depending on what format you want

d['a'] = 1
d['b'] = 2

print(d['a'])
print(d['c'])