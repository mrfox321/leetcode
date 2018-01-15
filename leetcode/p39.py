
class comb():

    def __init__(self):
        self.combo = {}

    def combinationSum(self,size,target,nums):
        #nums are sorted already
        if size == 1:
            if target in nums:
                return set((target,))
            else:
                return set(set())
        if (size,target) in self.combo:
            return self.combo[size,target]

        set_set = set()
        for i in xrange(len(nums)):
            if nums[i] <= target//2:
                if target - nums[i] >= 0:
                    combos = self.combinationSum(size-1,target-nums[i],nums)
                    for sets in combos:
                        a = [nums[i]]+list(sets)
                        a = set(a.sort)
                        set_set.add(a)
        combos = self.combinationSum(size-1,target,nums)
        for sets in combos:
            set_set.add(sets)
        self.combo[(size,target)] = set_set
        return set_set




nums = [1,3,4,6]
target = 8

size = target//nums[0]
x = comb()
print x.combinationSum(size,target,nums)
