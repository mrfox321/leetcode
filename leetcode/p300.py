def increaseSub(nums):

    if not nums:
        return 0
    if len(nums) == 1:
        return 1
    score = []
    score.append(1)
    maxscore = 1
    for i in xrange(1,len(nums)):
        newscore = 1
        for j in xrange(i):
            if nums[i] > nums[j]:
                newscore = max(newscore,score[j]+1)
        score.append(newscore)
        maxscore = max(maxscore,newscore)

    print score
    return maxscore

nums = [10,9,2,5,3,7,101,18]

print increaseSub(nums)
