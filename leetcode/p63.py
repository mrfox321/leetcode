def uniPath(grid,i,j,table):
    if grid[i][j] == 1:
        return 0
    if (i,j) in table:
        return table[i,j]
    m = len(grid) #rows
    n = len(grid[0]) #columns

    if i == m-1 and j == n-1:
        return 1


    score = 0
    if i+1 <= m-1:
        score += uniPath(grid,i+1,j,table)
    if j+1 <= n-1:
        score += uniPath(grid,i,j+1,table)
    table[i,j] = score
    return score

table = {}
print uniPath([[0,0]],0,0,table)
