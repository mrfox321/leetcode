def primes(n):
    sieve = [True]*n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def isDuplicate(numbers,new_number,prime,hashIndex):
    count = 1
    for num in numbers:
        count *= prime[hashIndex[num]]
    count *= prime[hashIndex[new_number]]

    return count

def subsets(nums):
    prime = primes(100)
    hashCombo = {}
    hashIndex = {}
    combos = []
    for index, num in enumerate(nums):
        hashIndex[num] = index
        hashCombo[prime[hashIndex[num]]] = 1
    combos = [[i] for i in nums]
    old_combo = combos[:]
    while len(combos[-1]) < len(nums):
        new_combo = []
        for numbers in old_combo: #[a1,a2....ak]
            for new_number in nums:
                if new_number not in numbers:
                    collision = isDuplicate(numbers,new_number,prime,hashIndex)
                    if collision not in hashCombo:
                        hashCombo[collision] = 1
                        combobreaker = numbers + [new_number]
                        new_combo.append(combobreaker)
                        #print numbers,new_combo
        combos += new_combo
        old_combo = new_combo
        if not new_combo:
            break
    return combos+[[]]


print subsets([1,3,6])
