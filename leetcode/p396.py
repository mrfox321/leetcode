def maxRot(nums):

    if not nums or len(nums) == 1:
        return 0

    summ = sum(nums)
    n = len(nums)

    #initialize F(0)
    prod = 0
    for i in xrange(len(nums)):
        prod += i*nums[i]
    prod_max = prod

    for i in xrange(len(nums)-1):
        last_digit = nums[-1-i]
        prod += summ - n*last_digit
        print prod
        prod_max = max(prod,prod_max)

    return prod_max


print maxRot([4,3,2,6])
