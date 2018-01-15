# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def build_list(l3):
    old_link = ListNode(l3[len(l3)])
    for i in reversed(xrange(len(l3)-1)):
        new_link = ListNode(l3[i])
        new_link.next = old_link
        old_link = new_link
    return old_link





class Solution(object):


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l3 = {}
        count = 0
        while True:
            l3[count] = (carry + l1.val + l2.val)%10

            if l1.val + l2.val < 10:
                carry = 0
            else:
                carry = 1

            if l1.next == None and l2.next == None:
                if carry == 0:
                    break
                else:
                    l3[count+1] = carry
                    break
            elif l1.next == None and l2.next != None:
                l1.next = ListNode(0)
            elif l1.next != None and l2.next == None:
                l2.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next
            count += 1
        return build_list(l3)
