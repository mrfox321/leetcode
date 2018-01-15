class TreeNode():
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None

def genBST(nums):


    if len(nums) == 1:
        x = TreeNode(nums[0])
        return [x]
    if len(nums) == 0:
        return [None]
    listoftrees = []
    for num in nums:
        left = [x for x in nums if x < num]
        right = [x for x in nums if x > num]
        leftdummy = genBST(left)
        rightdummy = genBST(right)
        print len(leftdummy),len(rightdummy),left,right
        for lefty in leftdummy:
            for righty in rightdummy:
                rootdummy = TreeNode(num)
                rootdummy.left = lefty
                rootdummy.right = righty
                listoftrees.append(rootdummy)
        print len(listoftrees)
    return listoftrees
