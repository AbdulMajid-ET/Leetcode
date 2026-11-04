class Solution(object):
    def findTheArrayConcVal(self, nums):
        total = 0
        while len(nums) > 1:
            first = nums.pop(0)
            last = nums.pop()

            total += int(str(first) + str(last))

        if len(nums) == 1:
            total += nums[0]

        return total

# Completed with naseef 