class Solution(object):
    def moveZeroes(self, nums): # 0, 1, 0, 3, 12
        position = 0

        for n in nums:
            if n != 0:
                nums[position] = n
                position += 1

        while position < len(nums):
            nums[position] = 0
            position += 1