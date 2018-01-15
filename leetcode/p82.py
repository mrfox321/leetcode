def delDupe(head):

    headhead = ListNode('pointer')
    l1 = headhead
    if not head:
        return None
    headhead.next = head
    l2 = head
    if head.next == None:
        return head
    l3 = head.next

    if head.next.next == None:
        if head.val == l3.val:
            return None
        else:
            return head

    while True:
        if l2.val != l3.val:
            if l3.next != None:
                l1 = l2
                l2 = l3
                l3 = l3.next
                print l1.val,l2.val,l3.val
            else:
                return headhead.next
        else:
            while l2.val == l3.val:
                if l3.next != None:
                    l3 = l3.next
                else:
                    l1.next = None
                    return headhead.next
            #now l2.val != l3.val
            l1.next = l3
            l2 = l3
            if l3.next == None:
                return headhead.next
            l3 = l3.next
