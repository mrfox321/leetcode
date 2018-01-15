class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def writeList(nums,i):

    if i == len(nums):
        return

    node = ListNode(nums[i])

    node.next = writeList(nums,i+1)

    return node

def splitList3(head):

    l1 = head
    l2 = head

    count = 0
    while l2.next is not None:
        if count%2 == 1:
            l3 = l1
            l1 = l1.next
        l2 = l2.next
        count +=1


    l2 = l1.next
    l1.next = None
    l3.next = None

    return (head,l1,l2)

def sortedListToBST(head):

    if not head:
        return

    if head.next is None:
        root = TreeNode(head.val)
        return root

    if head.next.next is None:
        root = TreeNode(head.next.val)
        root.left = TreeNode(head.val)
        return root

    left,center,right = splitList3(head)
    root = TreeNode(center.val)
    root.left = sortedListToBST(left)
    root.right =sortedListToBST(right)
    return root

x = writeList([3,4,5],0)
head = sortedListToBST(x)
print head.left.val
