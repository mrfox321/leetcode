def robrob(nums):
    rob = {}
    if not nums:
        return 0

    rob[0] = nums[0]
    if len(nums) == 1:
        return rob[0]

    rob[1] = max(nums[0],nums[1])
    if len(nums) == 2:
        return rob[1]

    for i in xrange(2,len(nums)):
        rob[i] = max(rob[i-1],nums[i]+rob[i-2])

    return rob[len(nums)-1]
