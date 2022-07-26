from itertools import count, cycle, repeat

# count
for i in count(10):
    print(i)
    if i == 15:
        break

# cycle
a = [1, 2, 3]
for i in cycle(a):
    print(i)
    if i == 3:
        break

# repeat
for i in repeat(1, 10):
    print(i)