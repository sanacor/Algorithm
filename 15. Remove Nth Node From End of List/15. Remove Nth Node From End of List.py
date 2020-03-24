

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return None

        if head.next.next is None:
            if n == 1:
                head.next = None
            elif n == 2:
                head = head.next

            return head

        h = head
        lead = head

        for i in range(0, n):
            lead = lead.next

        if lead is None:
            head = head.next
            return head

        while(lead.next != None):
            lead = lead.next
            head = head.next

        head.next = head.next.next

        return h