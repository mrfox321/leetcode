def bitwiseAND(m,n):

    if m==n:
        return m
    mm = bin(m)[2:]
    nn = bin(n)[2:]

    if m == 0 or n == 0:
        return 0
    if len(mm) != len(nn):
        return 0

    zz = ''
    trigger = 0
    for i in xrange(len(mm)):
        if mm[i] == nn[i] and mm[i] == '1' and trigger == 0:
            zz +='1'
        elif mm[i] == nn[i] and mm[i] == '0' and trigger == 0:
            zz +='0'
        else: #if the leading digits do not match, 0s below.
            trigger = 1
            zz += '0'

    return int(zz,2)
