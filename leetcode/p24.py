def swapPairs(head):
    if not head:
        return []
    elif head.next == None: # single node
        return head
    elif head.next.next == None: #two nodes
        node1 = head.next
        node1.next = head
        node1.next.next = None
        return node1

    #initial swap for > 2 nodes
    node1 = head
    node2 = head.next
    #node swap
    node1.next = node2.next
    node2.next = node1
    head = node2
    #pointer shift
    node2 = node1.next
    if node2.next == None:
        return head

    while True:
        #check for end swap
        if node2.next.next == None:
            node1.next = node2.next
            node1.next.next = node2
            node2.next = None
            return head
        #middle swaps
        node1.next = node2.next
        node2.next = node2.next.next
        node1.next = node2
        #pointer shift
        node1 = node2
        node2 = node2.next
        if node2.next == None:
            return head
