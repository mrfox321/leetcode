def quadHash(quad,hashindex,prime):
    qhash = 1
    for singlet in quad:
        qhash *= prime[hashindex[singlet]]
    return qhash

def isValid(quad,numcount):
    newcount = numcount.copy()
    for num in quad:
        if num in numcount:
            newcount[num] += -1
            if newcount[num] < 0:
                return False
        else:
            return False
    return True

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

def fourSum(nums,target):
    #frequency hash
    prime = primes(3000)
    numcount = {}
    for num in nums:
        if num not in numcount:
            numcount[num] = 1
        else:
            numcount[num] += 1
    #map from num to index, will use as prime[hashIndex[num]]
    hashIndex = {}
    for index,num in enumerate(nums):
        if num not in hashIndex:
            hashIndex[num] = index
    #hash for target - c - d that we will check with a + b
    hashsum = {}
    for cc in xrange(len(nums)):
        for dd in xrange(cc+1,len(nums)):
            c = nums[cc]
            d = nums[dd]
            if target - c - d not in hashsum:
                hashsum[target-c-d] = [[c,d]]
            else:
                hashsum[target-c-d].append([c,d])

    #check a + b = target - c - d
    foursolve = []
    fourhash = {}
    for aa in xrange(len(nums)):
        for bb in xrange(aa+1,len(nums)):
            a = nums[aa]
            b = nums[bb]
            if a+b in hashsum:
                for pair in hashsum[a+b]:
                    quad = [a,b]+pair
                    qhash = quadHash(quad,hashIndex,prime)
                    if isValid(quad,numcount) and qhash not in fourhash:
                        foursolve.append(quad)
                        fourhash[qhash] = 1
    return foursolve

nums = [1, 0, -1, 0, -2, 2]
target = 0
print fourSum(nums,target)
