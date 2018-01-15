import collections

def upGrid(grid):
    table = {}
    queue = collections.deque()
    m = len(grid)
    n = len(grid[0])
    for i in xrange(m):
        for j in xrange(n):
            if grid[i][j] == 0:
                table[i,j] = 0 #distance,marker
                queue.appendleft((i,j))

    while queue:
        u = queue.pop()
        i,j = u[0],u[1]
        if i > 0 and grid[i-1][j] != 0 and (i-1,j) not in table:
            table[i-1,j] = table[i,j] + 1
            queue.appendleft((i-1,j))
        if i < m-1 and grid[i+1][j] != 0 and (i+1,j) not in table:
            table[i+1,j] = table[i,j] + 1
            queue.appendleft((i+1,j))
        if j > 0 and grid[i][j-1] != 0 and (i,j-1) not in table:
            table[i,j-1] = table[i,j] + 1
            queue.appendleft((i,j-1))
        if j < n-1 and grid[i][j+1] != 0 and (i,j+1) not in table:
            table[i,j+1] = table[i,j] + 1
            queue.appendleft((i,j+1))

    new_grid = [[table[i,j] for j in xrange(n)] for i in xrange(m)]
    return new_grid

print upGrid([[0],[0],[0],[0]])
