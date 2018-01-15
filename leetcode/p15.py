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
                hashsum[twosum].append(nums[i],nums[j])

    for k in xrange(len(nums)):
        if -c in hashsum


def threeSum(nums):

    nums.sort()
    ans = []
    for i in xrange(len(nums)-2):
        a = nums[i]
        if a > 0:
            break
        j = i+1
        k = len(nums)-1
        if i > 0 and nums[i] == nums[i-1]:
            continue
        while True:

            if j == k:
                break
            b = nums[j]
            c = nums[k]

            if a + b + c > 0:
                k += -1
            elif a + b + c < 0:
                j += 1
            elif a + b + c == 0:
                ans.append([a,b,c])
                while nums[j] == b and j < k:
                    j += 1

    return ans
