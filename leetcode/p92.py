def reverseList(head):

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

def revMid(head,m,n):

    if m == n:
        return head

    if m == 1: #don't need pointer before mid
        l1 = head
        l2 = head

        count = 1
        while count < n:
            l2 = l2.next
            count += 1

        if l2.next == None: #basic reversed list
            return reverseList(l1)

        l3 = l2.next
        l2.next = None
        mid = reverseList(l1)
        l1.next = l3
        return mid

    else:
        l1 = head
        l3 = head

        count = 1
        while count < n:
            l3 = l3.next
            if count < m - 1:
                l1 = l1.next
            count += 1

        l2 = l1.next
        if l3.next == None:
            l1.next = reverseList(l2)
            return head

        else:
            l4 = l3.next
            l1.next == None
            l3.next == None

            l1.next = reverseList(l2)
            l2.next = l4

            return head
