# basically makes expression based functions easier

add10 = lambda x: x + 10
print(add10(5))

mulxy = lambda x, y: x*y
print(mulxy(5,5))


points2D = [(1,2),(15,1),(5,-1),(10,4)]
# sorts a list by the x element (first element)
p2d_sorted = sorted(points2D)

print(points2D)
print(p2d_sorted)

points2D = [(1,2),(15,1),(5,-1),(10,4)]
# sorts a list by the function... here list is sorted by second elem in the tuple
p2d_sorted = sorted(points2D, key=lambda x: x[1])

print(points2D)
print(p2d_sorted)

# sorts by the sum of each tuple
p2d_sorted = sorted(points2D, key=lambda x: x[0]+x[1])
print(p2d_sorted)