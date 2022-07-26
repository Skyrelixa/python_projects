number_grid = [
   # 0 1 2
    [1,2,3], # row0
    [4,5,6], # row1
    [7,8,9], # row2
    [0]      # row3
]

print(number_grid[0][0]) # row, column

for row in number_grid:
    for column in row:
        print(column)