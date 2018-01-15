def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    tail = head
    while tail.next != None:
        tail.val = 'cycle'
        tail = tail.next
        if tail.val == 'cycle':
            return True
    return True
