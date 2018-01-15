def wiggle(nums):

    if not nums:
        return 0

    wig = 1
    count = 0
    for i in xrange(1,len(nums)):
        if nums[i] != nums[i-1]:
            if nums[i] > nums[i-1]:
                pol = -1
            elif nums[i] < nums[i-1]:
                pol = 1
            count = i
            wig += 1
            break
    if count == 0:
        return wig

    for i in xrange(count+1,len(nums)):
        if pol*(nums[i] - nums[i-1]) > 0:
                wig += 1
                pol *= -1

    return wig


print wiggle([1,1,1,1,2,2,1])
