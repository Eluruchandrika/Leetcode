class Solution:
    def maxSubArray(self, nums):
        curr = 0
        maxVal = nums[0]

        for i in nums:
            if curr <0:
                curr=0
            curr+=i
            if curr>maxVal:
                maxVal = curr
        return maxVal
        