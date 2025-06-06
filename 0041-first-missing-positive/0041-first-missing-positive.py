class Solution:
    def firstMissingPositive(self, nums):
        n= len(nums)

        for i in range(n):

            while 1 <= nums[i] <= n and nums[i] != nums[nums[i]-1]:
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
            
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        
        return n+1


        