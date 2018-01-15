def inSwap(nums):

    for i in xrange(len(nums)):
        j = i
        while j > 0 and str(nums[j-1])+str(nums[j]) < str(nums[j])+str(nums[j-1]):
            nums[j-1],nums[j] = nums[j],nums[j-1]
            j += -1
        i += 1

    return str(int(''.join(str(x) for x in nums)))
