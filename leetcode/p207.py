def canFinish(numC,prereqs):
    #construct dict of directed edges
    edges = {}
    for prereq in prereqs:
        if prereq[0] not in edges:
            edges[prereq[0]] = [prereq[1]]
        else:
            edges[prereq[0]].append(prereq[1])

    cycles = {}
    for i in xrange(numC):
        if isCycle(i,cycles,edges,[]): #is there is a cycle
            return False #cannot complete courses

    return True


def isCycle(num,cycles,edges,path):

    if num in cycles:
        return False


    path.append(num)
    #end of the road
    if num not in edges:
        cycles[num] = False
        return False

    #go deeper
    for req in edges[num]:
        if req in path:
            return True

        if isCycle(req,cycles,edges,path[:]):
            return True

    cycles[num] = False
    return False

numC = 4
pre = [[0,1],[1,2],[2,0]]
print canFinish(numC,pre)
