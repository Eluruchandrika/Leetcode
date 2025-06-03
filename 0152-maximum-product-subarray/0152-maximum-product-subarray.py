class Solution:
    def maxProduct(self, nums):
        currMax= nums[0]
        currMin = nums[0]
        maxProd=nums[0]

        for i in range(1,len(nums)):
            temp = max(nums[i],currMax*nums[i],currMin*nums[i])
            currMin = min(nums[i] , currMax*nums[i],currMin*nums[i])

            currMax=temp
            maxProd= max(currMax,maxProd)
        return maxProd        