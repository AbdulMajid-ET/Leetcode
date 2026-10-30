class Solution(object):
    def runningSum(self, nums):

        result = []

        for i in range(len(nums)):
            total = 0

            for j in range(i + 1):
                total += nums[j]

            result.append(total)

        return result