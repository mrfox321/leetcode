class comb():

    def __init__(self):
        self.combo = {}

    def cSum(self,size,target,nums):
        #memoization
        set_set = set()
        if not nums or nums[0] > target:
            return set_set
        if (size,target) in self.combo:
            return self.combo[(size,target)]
        #nums are sorted already
        if size == 1:
            if target in nums:
                set_set.add((target,))
                self.combo[(size,target)] = set_set
                return set_set
            else:
                set_set.add(())
                self.combo[(size,target)] = set_set
                return set_set

        for i in xrange(len(nums)):
            if nums[i] <= target//2 and target - nums[i] >= 0:
                combos = self.cSum(size-1,target-nums[i],nums)
                for tuples in combos:
                    if tuples:
                        set_set.add(tuple(sorted([nums[i]]+list(tuples))))
        combos = self.cSum(size-1,target,nums)
        for tuples in combos:
            if tuples:
                set_set.add(tuples)
        self.combo[(size,target)] = set_set
        return set_set


class Solution(object):
    def combinationSum(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        size = target//nums[0]
        x = comb()
        y = x.cSum(size,target,nums)
        z = [list(tuples) for tuples in y]
        if z == [[]]:
            return []
        return z
