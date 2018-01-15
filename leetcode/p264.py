def uglyNum(n):

    i = 0
    j = 0
    k = 0

    num = []
    num.append(1)
    if n == 1:
        return num

    for index in xrange(1,n):

        x1 = 2*num[i]
        x2 = 3*num[j]
        x3 = 5*num[k]

        x_min = min(x1,x2,x3)
        num.append(x_min)

        if x_min == x1:
            i += 1
        if x_min == x2:
            j += 1
        if x_min == x3:
            k += 1
    return num

print uglyNum(10)
