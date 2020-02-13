
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length

        result = []
        for i in range(length):
            idx = self.get_idx(i, k, length)
            result.append(nums[idx])

        for i in range(length):
            nums[i] = result[i]

    def get_idx(self, i, k, length):
        if i - k > -1:
            return i - k
        else:
            return length + (i - k)


if __name__ == '__main__':
    # nums = [1,2,3,4,5,6,7]
    # k = 3

    nums = [-1, -100, 3, 99]
    k = 2
    print(nums)

    sol = Solution()
    nums = sol.rotate(nums, k)
    print(nums)
