class Solution:
    def maxSubArray(self, nums):
        curr = nums[0]
        maxVal = nums[0]

        for i in range(1,len(nums)):
            curr=max(nums[i],curr+nums[i])
            maxVal=max(maxVal,curr)
        return maxVal
        