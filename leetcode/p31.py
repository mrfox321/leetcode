def nextPerm(nums):
    for i in xrange(1,len(nums)):
        diff = 10239802398
        for j in xrange(i):
            if nums[-1-i] < nums[-1-j]:
                new_diff = nums[-1-j] - nums[-1-i]
                if new_diff < diff:
                    diff = new_diff
                    index = j
        if diff != 10239802398:
            nums[-1-i],nums[-1-index] = nums[-1-index],nums[-1-i]
            nums[-i:] = sorted(nums[-i:])
            return

    nums.sort()
    return

x = [4,2,0,2,3,2,0]
nextPerm(x)

print x
