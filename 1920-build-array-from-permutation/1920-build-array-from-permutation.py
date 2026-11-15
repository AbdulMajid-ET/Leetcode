class Solution(object):
    def buildArray(self, nums):
        ans = [] 

        for i in range(len(nums)):
            value = nums[i]
            result = nums[value]    
            ans.append(result)      

        return ans