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


def reorderList(head):

    if head == None:
        return
    if head.next == None:
        return
    if head.next.next == None:
        return

    #gets to end of first list
    l1 = head
    #moves to end of entire list
    l2 = head
    count = 0
    while l2.next != None:
        l2 = l2.next
        count += 1
        if count%2 == 0:
            l1 = l1.next
    #move pointer to head of second list
    l2 = l1.next
    #split lists
    l1.next = None

    #set head of split lists
    l1 = head
    l2 = reverseList(l2)

    #splice together the lists
    while True:
        if l1.next != None and l2.next != None:
            l3 = l1.next
            l4 = l2.next

            l1.next = l2
            l2.next = l3

            l1 = l3
            l2 = l4
        if l1.next == None and l2.next == None:
            l1.next = l2
            return

        if l1.next != None and l2.next == None:
            l3 = l1.next
            l1.next = l2
            l2.next = l3
            return 
