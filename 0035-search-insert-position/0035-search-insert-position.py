class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
                # which gives us the targeted value index 5 >= 5 

        return len(nums)
        # this is for 3rd example if we not found the target number in the list 
        # so return its index where to insert in the list here at 4th index so the 7 comes last of list