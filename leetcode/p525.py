def equal01(nums):

    table = {}
    table[0] = -1
    count = 0
    score = 0
    for i in xrange(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1
        if count not in table:
            table[count] = i
        else:
            score = max(score,i - table[count])

    return score
