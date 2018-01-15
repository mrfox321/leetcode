# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        while True:
            l3 = ListNode(carry + l1.val + l2.val)

            if l1.val + l2.val < 10:
                carry = 0
            else:
                carry = 1

            if l1.next == None and l2.next == None:
                if carry == 0:
                    break
                else:
                    l3.next = ListNode(carry)
                    break
            elif l1.next == None and l2.next != None:
                l1.next = ListNode(0)
            elif l1.next != None and l2.next == None:
                l2.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
            return l3
