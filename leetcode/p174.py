def dungeonMaster(grid,table,i,j):

    if (i,j) in table:
        return table[i,j]

    m = len(grid)
    n = len(grid[0])

    if i+1 == m and j+1 == n:
        table[i,j] = max(1,1-grid[i][j])
        return table[i,j]

    #can move right+down
    if i+1 < m and j+1 < n:
        table[i,j] = max(1,min(dungeonMaster(grid,table,i,j+1),dungeonMaster(grid,table,i+1,j))-grid[i][j])
        return table[i,j]

    #can only move right
    if i+1 == m and j+1 < n:
        table[i,j] = max(1,dungeonMaster(grid,table,i,j+1)-grid[i][j])
        return table[i,j]

    #can only move down
    if i+1 < m and j+1 == n:
        table[i,j] = max(1,dungeonMaster(grid,table,i+1,j)-grid[i][j])
        return table[i,j]

grid = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
table = {}
print dungeonMaster(grid,table,0,0)
