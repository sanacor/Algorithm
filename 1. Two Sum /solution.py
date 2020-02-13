class Solution(object):
    def twoSum(self, nums, target):
        # print(target)
        for i in range(0, len(nums)):
            # print(nums[i])
            # if nums[i] > target:
            #     continue

            for k in range(i+1, len(nums)):
                # print(nums[k])
                # if nums[k] > target:
                #     continue

                if target == nums[i] + nums[k]:
                    return [i, k]

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    nums = [-3,4,3,90]
    target = 9
    target = 0
    s = Solution()
    s.twoSum(nums, target)