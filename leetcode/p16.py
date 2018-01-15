def threeNear(nums,target):

    nums.sort()
    ans = []
    min_diff = 939393939393
    diff = 939393939393
    for i in xrange(len(nums)-2):
        a = nums[i]

        j = i+1
        k = len(nums)-1
        if i > 0 and nums[i] == nums[i-1]:
            continue
        while True:

            if j == k:
                break
            b = nums[j]
            c = nums[k]
            diff = target - a - b - c
            if abs(diff) < abs(min_diff):
                min_diff = diff
            if a + b + c > target:
                k += -1
            elif a + b + c < target:
                j += 1
            elif a + b + c == target:
                return a + b + c

    return target - min_diff

print threeNear([1,1,1,1],0)
