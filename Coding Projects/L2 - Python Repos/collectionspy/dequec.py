# can be used to add or remove elements
from collections import deque

d = deque()

d.append(1)
d.append(2)

d.appendleft(3)

print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
d.extend([1, 2, 3])
print(d)

d.extendleft([4, 5, 6])
print(d)

d.rotate(1)
print(d)

d.rotate(-1)
print(d)

d.reverse()
print(d)