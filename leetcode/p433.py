import collections

def compareDNA(string1,string2):
    count = 0
    for i in xrange(len(string1)):
        if string1[i] != string2[i]:
            count+= 1

    if count == 1:
        return True
    return False


def minPath(start,end,bank):

    if end not in bank:
        return -1

    #initialize
    dna = {}
    dna[0] = [start,[],0,0] #[DNA,neighbors,dist,color]
    for index,string1 in enumerate(bank):
        if compareDNA(start,string1):
            dna[0][1].append(index+1)
    print dna[0]

    for index1,string1 in enumerate(bank):
        dna[index1+1] = [string1,[],-1,0]
        for index2,string2 in enumerate(bank):
            if string1 != string2 and compareDNA(string1,string2):
                dna[index1+1][1].append(index2+1)


    #begin DfS
    start = dna[0]

    queue = collections.deque()
    queue.appendleft(start)

    while queue:
        u = queue.pop()
        for index in u[1]:
            v = dna[index]
            if v[3] == 0:
                v[3] = 1
                v[2] = u[2] + 1
                if v[0] == end:
                    return v[2]
                queue.appendleft(v)
        u[3] = 2

    return -1

start="AACCGGTT"
end="AACCGGTA"
bank= ["AACCGGTA"]
print minPath(start,end,bank)
