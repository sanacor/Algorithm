# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self, x):
        self.of = None
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        while True:
            v_l1 = l1.val
            v_l2 = l2.val

            v_sum, self.of = self._get_sum_and_of(v_l1, v_l2)

            list_node = ListNode(v_sum)

    def _get_sum_and_of(self, v_l1, v_l2):
        if v_l1 + v_l2 > 9:
            return (v_l1 + v_l2 / 10, True)
        else:
            return (v_l1 + v_l2 / 10, False)

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    nums = [-3,4,3,90]
    target = 9
    target = 0
    s = Solution()
    s.twoSum(nums, target)