def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head.next == None:
        return head

    l1 = head
    l2 = head.next
    #len(list) = 2
    if head.next.next == None:
        l1.next = None
        l2.next = l1
        return l2

    l3 = head.next.next

    l1.next = None
    while True:
        l2.next = l1
        if l3.next == None:
            l3.next = l2
            return l3
        l1 = l2
        l2 = l3
        l3 = l3.next
