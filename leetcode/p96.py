class numnum():

    def __init__(self):
        self.tree = {}
        self.tree[0] = 1
        self.tree[1] = 1

    def numBST(self,nums):
        if len(nums) in self.tree:
            return self.tree[len(nums)]
        count = 0
        for num in nums:
            left = [x for x in nums if x < num]
            right = [x for x in nums if x > num]

            score = self.numBST(left)*self.numBST(right)
            count += score
            print score,left,right
        self.tree[len(nums)] = count
        return count
x = numnum()
print x.numBST(range(6))
