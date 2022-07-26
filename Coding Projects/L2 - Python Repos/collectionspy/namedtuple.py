from collections import namedtuple

# creates a class Point with params x, y
Point = namedtuple('Point', 'x,y')

pt = Point(1, 4)
print(pt)           # can also use pt.x and pt.y to get nums of coords