# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and l2:
            return l2
        elif not l2 and l1:
            return l1
        elif not l1 and not l2:
            return []

        head = ListNode(69)
        tail = head
        while True:
            if l1.val <= l2.val:
                tail.next = l1
                if l1.next == None:
                    tail.next.next = l2
                    return head.next
                else:
                    tail = tail.next
                    l1 = l1.next
            else:
                tail.next = l2
                if l2.next == None:
                    tail.next.next = l1
                    return head.next
                else:
                    tail = tail.next
                    l2 = l2.next
