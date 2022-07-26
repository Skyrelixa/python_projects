# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
# note: when importing a module, your python file cannot be the name of the module

from collections import Counter
a = "aaaaabbbbbccccdddd"
mycounter = Counter(a)
print(mycounter)

# in parentheses, determines how many most common elements I want
print(mycounter.most_common(2)[1][1])     # [index of tuple][elem in tuple]

print(list(mycounter.elements()))