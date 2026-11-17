class Solution(object):
    def twoSum(self, nums, target):

        for i in range(len(nums)): # [2, 7, 11, 15]
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]