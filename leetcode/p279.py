def perfSquare(n):

    squares = [x**2 for x in xrange(1,int(n**0.5)+1)]
    x = {}
    x[0] = 0
    for i in xrange(1,n+1):
        square = squares[:int(i**0.5)]
        diff = [1+x[i-num] for num in square]
        x[i] = min(diff)
    return x[n]
