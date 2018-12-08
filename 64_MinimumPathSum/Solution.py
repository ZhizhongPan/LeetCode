def dp(grid):
    for row in range(1, len(grid)):
        grid[row][0] += grid[row-1][0]
    
    for col in range(1, len(grid[0])):
        grid[0][col] += grid[0][col-1]
    
    for row in range(1, len(grid)):
        for col in range(1, len(grid[0])):
            grid[row][col] += min(grid[row-1][col], grid[row][col-1])
    
    return grid[-1][-1]

def dp2(grid):
    cur = [grid[0][0]] * len(grid)
    for row in range(1, len(grid)):
        cur[row] = cur[row-1] + grid[row][0]

    for col in range(1, len(grid[0])):
        cur[0] += grid[0][col]
        for row in range(1, len(grid)):
            cur[row] =  min(cur[row-1], cur[row]) + grid[row][col]
    
    return cur[-1]
