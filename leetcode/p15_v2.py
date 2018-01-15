def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def hashFreq(nums):

    freq = {}
    for i in xrange(nums):
        if nums[i] not in freq:
            freq[i] = 1
        else:
            freq[i] += 1

    return freq



def three_Sum(nums):
    #frequency table
    freq = {}
    for i in xrange(nums):
        if nums[i] not in freq:
            freq[i] = 1
        else:
            freq[i] += 1

    hashsum = {}
    for i in xrange(len(nums)):
        for j in xrange(i+1,len(nums)):
            twosum = nums[i] + nums[j]
            if twosum not in hashsum:
                hashsum[twosum] = (nums[i],nums[j])
            else:
                hashsum[twosum].append((nums[i],nums[j]))

    for k in xrange(len(nums)):
        if -c in hashsum:
            #check we have enough
