def maxSubarray(nums):
    current_max = nums[0]
    max_end = nums[0]

    for i in xrange(1,len(nums)):
        max_end = max(max_end+nums[i],nums[i])
        current_max = max(max_end,current_max)
    return current_max
