# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):

        while node is not None and node.next is not None:
            node.val = node.next.val
            node = node.next

        node = None
