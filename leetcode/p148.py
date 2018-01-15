class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def mergeList(left,right):

    root = ListNode(0)

    head = root

    while True:

        if left.val <= right.val:
            if left.next is None:
                head.next = left
                head.next.next = right
                return root.next

            else:
                l2 = left.next
                left.next = None
                head.next = left
                left = l2
                head = head.next
        else:
            if right.next is None:
                head.next = right
                head.next.next = left
                return root.next
            else:
                l2 = right.next
                right.next = None
                head.next = right
                right = l2
                head = head.next

def writeList(nums,i):

    if i == len(nums):
        return

    node = ListNode(nums[i])

    node.next = writeList(nums,i+1)

    return node

def readList(head,nums):

    nums.append(head.val)

    if head.next is None:
        return nums

    return readList(head.next,nums)

def splitList(head):

    l1 = head
    l2 = head

    count = 0
    while l2.next is not None:
        if count%2 == 1:
            l1 = l1.next
        l2 = l2.next
        count +=1


    l2 = l1.next
    l1.next = None

    return (head,l2)

def mergeSort(head):

    if head.next is None:
        return head

    left,right = splitList(head)

    left = mergeSort(left)
    right = mergeSort(right)

    return mergeList(left,right)


x = writeList([3,2,1],0)



print readList(x,[])
x = mergeSort(x)
print readList(x,[])
