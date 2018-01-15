def findCycle(head):

     if not head:
            return None
        if head.next is None:
            return None
        l1 = head
        l2 = head

        while True:
            l1 = l1.next
            if l2.next is None:
                return None

            l2 = l2.next
            if l2.next is None:
                return None
            l2 = l2.next

            if l1 is l2:
                break

        l1 = head
        if l1 is l2:
            return l1
        while True:
            l1 = l1.next
            l2 = l2.next
            if l1 is l2:
                return l1
