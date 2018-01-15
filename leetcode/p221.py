def maxSquare(grid):

    m = len(grid) #rows
    n = len(grid[0]) #columns
    dim = min(m,n)
    table = {}
    score = [0]
    if dim == m and m < n: #stide by columns
        for j in xrange(n-m+1):
            isSquare(grid,dim,0,j,score,table)
    if dim == n and n < m: #stride by rows
        for i in xrange(m-n+1):
            isSquare(grid,dim,i,0,score,table)
    else:
        isSquare(grid,dim,0,0,score,table)

    return score[0]**2

def isSquare(grid,level,i,j,score,table):
    if (level,i,j) in table:
        return table[level,i,j]
    if level == 1:
        if grid[i][j] == '1':
            score[0] = max(level,score[0])
            return True
        else:
            return False

    space = [isSquare(grid,level-1,i+m,j+n,score,table) for m in xrange(2) for n in xrange(2)]
    if False in space:
        table[level,i,j] = False
        return False
    else:
        score[0] = max(level,score[0])
        table[level,i,j] = True
        return True
