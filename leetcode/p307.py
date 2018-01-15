def segTree(root,nums):

    if root.start == root.end:
        root.data = nums[root.start]
        return

    center = (root.start+root.end)//2

    root.left = SegNode(root.start,center)
    root.left.parent = root
    root.right = SegNode(center+1,root.end)
    root.right.parent = root

    segTree(root.left,nums)
    segTree(root.right,nums)

    root.data = root.left.data + root.right.data


def update(i,val,head):

    root = head
    if i < root.start or i > root.end:
        return

    while True:

        if root.start == root.end:
            diff = val - root.data
            root.data += diff
            break

        elif i <= root.left.end:
            root = root.left
        else:
            root = root.right


    while root.parent is not None:
        root = root.parent
        root.data += diff

def sumRange(i,j,root):

    if i == root.start and j == root.end:
        return root.data

    if i <= root.left.end and j >= root.right.start:
        return sumRange(i,root.left.end,root.left) + sumRange(root.right.start,j,root.right)

    if i <= root.left.end and j <= root.left.end:
        return sumRange(i,j,root.left)

    if i >= root.right.start and j >= root.right.start:
        return sumRange(i,j,root.right)


class SegNode():

    def __init__(self,start,end):

        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.data = None
        self.parent = None


nums = []
root = SegNode(0,len(nums)-1)
segTree(root,nums)
for i in xrange(len(nums)):
    for j in xrange(i):
        print sumRange(j,i,root)==sum(nums[j:i+1])
update(14,0,root)
nums[14] = 0
for i in xrange(len(nums)):
    for j in xrange(i):
        print sumRange(j,i,root)==sum(nums[j:i+1])
