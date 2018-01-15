def robrob(nums):
    rob = {}
    if not nums:
        return 0

    rob[0] = nums[0]
    if len(nums) == 1:
        return (rob[0],True)

    rob[1] = max(nums[0],nums[1])
    if len(nums) == 2:
        return (rob[1],True)

    for i in xrange(2,len(nums)):
        rob[i] = max(rob[i-1],nums[i]+rob[i-2])

    end = len(nums)-1
    if rob[end] == nums[i]+rob[i-2]:
        occupied = True
    else:
        occupied = False

    return (rob[end],occupied)

def robrobrob(nums):
    score_right = robrob(nums)
    score_left = robrob(nums[::-1])
    score = score_right[0]
    right = score_right[1]
    left = score_left[1]

    if right == True and left == True:
        score_right = robrob(nums[:-1])
        score_left = robrob(nums[1:])
        return max(score_right[0],score_left[0])

    else:
        return score


print robrobrob([6,6,6])
