def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def isDuplicate(numbers,new_number,prime):
    count = 1
    for num in numbers:
        count *= prime[num]
    count *= prime[new_number]

    return count


def combo(n,k):
    prime = primes(200)

    hashCombo = {}
    for num in xrange(1,n+1):
        hashCombo[prime[num]] = 1
    #initialize
    combos = [[i] for i in xrange(1,n+1)]
    for size in xrange(1,k):  #build up to k-choices
        new_combo = []
        for numbers in combos: #[a1,a2....ak]
            for new_number in xrange(1,n+1):
                if new_number not in numbers:
                    collision = isDuplicate(numbers,new_number,prime)

                    if collision not in hashCombo:
                        hashCombo[collision] = 1
                        combobreaker = numbers + [new_number]
                        new_combo.append(combobreaker)
                        print combobreaker
                        #print numbers,new_combo
        combos = new_combo
    return combos

x = combo(13,5)
print x,len(x)
