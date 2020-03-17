# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    collection = []

    def hasCycle(self, head):
        """
        순회 하면서 이미 발견된 노드가 다시 나오는 경우를 순환으로 판단하기
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False

        if head not in Solution.collection:
            Solution.collection.append(head)
            return self.hasCycle(head.next)
        else:
            return True
