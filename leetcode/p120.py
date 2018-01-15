def minTri(triangle):
    #bottom up approach
    minpath = triangle[-1]
    for i in xrange(1,len(triangle)):
        new_min = [0 for j in xrange(len(triangle)-i)]
        for j in xrange(len(triangle)-i):
            new_min[j] = triangle[-1-i][j] + min(minpath[j],minpath[j+1])
        minpath = new_min
    return minpath[0]
