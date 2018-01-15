def countBits(n):

    count = []
    count.append(0)
    count.append(1)

    for i in xrange(2,n+1):
        count.append(count[i//2])
        if i%2 == 1:
            count[i] += 1
    return count

print countBits(5)
