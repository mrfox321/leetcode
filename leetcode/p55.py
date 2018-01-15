class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = nums[::-1]
        F = {}
        F[0] = True

        for i in xrange(1,len(nums)):
            F[i] = False
            if nums[i] == 0:
                F[i] = False
            else:
                count = 0
                for j in xrange(max(0,i-nums[i]),i):
                    if F[j] == True:
                        F[i] = True
        return F[len(nums)-1]


            
