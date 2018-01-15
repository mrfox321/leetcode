def minSubLens(s,nums):

    sumarr = []
    current_sum = 0
    #create sum
    for i in xrange(0,len(nums)):
        current_sum += nums[i]
        sumarr.append(current_sum)

    if current_sum == s:
        return len(nums)
    if current_sum < s:
        return 0

    score = len(nums)+1
    #first index
    for j in xrange(len(nums)):
        if sumarr[j] >= s:
            score = min(score,j+1)
            break

    #two pointer strat
    for i in xrange(1,len(nums)):
        for j in xrange(min(i+score-2,len(nums)-1),i-1,-1):
            if sumarr[j] - sumarr[i-1] >= s:
                score = min(score,j-i+1)
            if sumarr[j] - sumarr[i-1] < s:
                break

    if score == len(nums) + 1:
        return 0

    return score
