def fact(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def getPermutation(n,k):
    ints = [i + 1 for i in range(n)]
    ans = []
    if n == 1:
        return '1'
    while True:
        for i in xrange(n):
            if i*fact(n-1)+1 <= k and k <= (i+1)*fact(n-1):
                ans.append(ints[i])
                del ints[i]
                k = k - i*fact(n-1)
                n = n-1
                if n == 1:
                    ans.append(ints[0])
                    str1 = ''.join(str(e) for e in ans)
                    return str1
                break

for i in range(1,fact(4)+1):
    print getPermutation(4,i)
