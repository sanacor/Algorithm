class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) == len(set(nums)):
            return False
        return True
        """
        :type nums: List[int]
        :rtype: bool
        """