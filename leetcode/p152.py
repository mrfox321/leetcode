def maxProduct(nums):
    current_max = nums[0]
    max_end = nums[0]
    min_end = nums[0]

    for i in xrange(1,len(nums)):
        min_end,max_end = min(max_end*nums[i],min_end*nums[i],nums[i]),max(max_end*nums[i],min_end*nums[i],nums[i])
        current_max = max(max_end,current_max)
    return current_max

print maxProduct([2,3])
