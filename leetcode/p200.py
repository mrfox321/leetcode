def numIsles(grid):

    land = {}
    new_land = {}
    count = 0
    for i in xrange(len(grid)):
        for j in xrange(len(grid[0])):
            if grid[i][j] == '1':
                if (i,j) not in land and (i,j) not in new_land:
                    count += 1
                    new_land[i,j] = [i,j]
                    while new_land:
                        state,value = new_land.popitem()
                        land[state] = value
                        m = state[0]
                        n = state[1]

                        if m > 0:
                            if (m-1,n) not in land and (m-1,n) not in new_land and grid[m-1][n] == '1':
                                new_land[m-1,n] = 0
                        if m < len(grid) - 1:
                            if (m+1,n) not in land and (m+1,n) not in new_land and grid[m+1][n] == '1':
                                new_land[m+1,n] = 0
                        if n > 0:
                            if (m,n-1) not in land and (m,n-1) not in new_land and grid[m][n-1] == '1':
                                new_land[m,n-1] = 0
                        if n < len(grid[0]) - 1:
                            if (m,n+1) not in land and (m,n+1) not in new_land and grid[m][n+1] == '1':
                                new_land[m,n+1] = 0


    return count
