def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    matrix = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        matrix[0][i] = 1
    print matrix[4][1]
    for i in range(1,m):
        for j in range(n):
            if j==0:
                matrix[i][j] = 1

            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    return matrix[m-1][n-1]

print uniquePaths(2,1)
