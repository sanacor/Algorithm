class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        last_index = len(nums) - 1
        k = k % length

        print('length: '+str(length))
        print('last_index: ' + str(last_index))
        print('k: '+str(k))

        if k == 0 or (k % length) == 0:
            return

        current_inx = 0
        tmp = nums[current_inx]

        for i in range(len(nums)):
            move_to_index = self.get_index_to_move(current_inx, k, last_index)
            now_val = tmp
            tmp = nums[move_to_index]
            current_inx = move_to_index
            nums[move_to_index] = now_val

    def get_index_to_move(self, current_inx, k, last_index):
        if current_inx + k > last_index:
            return current_inx + k - last_index - 1
        else:
            return current_inx + k


if __name__ == '__main__':
    # nums = [1,2,3,4,5,6,7]
    # k = 3

    nums = [-1, -100, 3, 99]
    k = 2
    sol = Solution()
    sol.rotate(nums, k)
    print(nums)