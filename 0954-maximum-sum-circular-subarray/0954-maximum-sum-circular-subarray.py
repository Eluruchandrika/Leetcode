class Solution:
    def maxSubarraySumCircular(self, nums):

        currMaxSum = 0
        maxSum=nums[0]
        currMinSum = 0
        minSum=nums[0]
        totalSum=0

        for i in range(len(nums)):
            # max subarray sum
            currMaxSum = max(nums[i],nums[i]+currMaxSum)
            maxSum = max(maxSum,currMaxSum)

            # min subarry sum

            currMinSum = min(nums[i] , nums[i] + currMinSum)
            minSum = min(minSum,currMinSum)

            totalSum+=nums[i]
        
        if minSum == totalSum:
            return maxSum
        return max(maxSum, totalSum-minSum)
