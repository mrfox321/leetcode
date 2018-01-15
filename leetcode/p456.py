def find132(nums):

    if len(nums) < 3:
        return False

    stack = [[nums[0],nums[0]]]
    for i in xrange(1,len(nums)):
        for interval in stack:
            if interval[0] < nums[i] and nums[i] < interval[1]:
                return True
            elif interval[1] < nums[i]:
                interval[1] = nums[i]

        if nums[i] < stack[-1][0]:
            if stack[-1][0] == stack[-1][1]:
                stack.pop()
                stack.append([nums[i],nums[i]])
            else:
                stack.append([nums[i],nums[i]])

    return False

print find132([1,3,2,0])
