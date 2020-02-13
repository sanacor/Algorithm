nums = [1, 1, 1, 3, 4, 4, 5, 6]

# nums = [1, 3, 1, 3, 4, 4, 5, 6]

len = len(nums)
saved = None
cnt = 0

for index, value in enumerate(nums):
    print(index, value)
    # index = index +
    for i in range(index + 1, len):
        if value == nums[i]:
            cnt = cnt + 1
        else:
            # saved = i
            nums[index+1] = nums[index+i]
            print()
            break


