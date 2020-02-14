class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cur = 0
        for idx, val in enumerate(nums):
            if nums[cur] == nums[idx]:
                continue
            else:
                cur=cur+1
                nums[cur] = nums[idx]

        return cur + 1


if __name__ == '__main__':
    nums = [1, 1, 2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    sol = Solution()
    length = sol.removeDuplicates(nums)
    print(length)
    print(nums)
