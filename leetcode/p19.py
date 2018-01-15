def removeNodeN(head,n):
    count = 0
    leadNode = head
    lagNode = None
    while True:
        if count == n:
            lagNode = head

        if leadNode.next == None:
            if count == 0:
                return []
            elif count == 1:
                if n==1:
                    print 'should be here'
                    head.next = None
                    return head
                else:
                    return leadNode
            if count == n-1: #remove head
                return head.next
            if lagNode.next.next != None: # n != 1
                lagNode.next = lagNode.next.next
            else:  #n = 1
                lagNode.next = None
            return head

        count += 1
        leadNode = leadNode.next
        if lagNode != None:
            lagNode = lagNode.next
