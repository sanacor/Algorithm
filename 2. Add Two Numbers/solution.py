# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        of = 0
        ln = ListNode(0)
        first = ln
        while l1 and l2:
            if l1.val + l2.val > 9:
                of = 1
                ln.val = ((l1.val + l2.val + of) % 10)
            else:
                ln.val = (l1.val + l2.val)
                of = 0
            //ln.val = (l1.val+l2.val) %10 + of
            //of = (l1.val+l2.val)/10

            ln.next = ListNode(0)
            ln = ln.next

            l1 = l1.next
            l2 = l2.next

        if of:
            ln.val = of

        return first