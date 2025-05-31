class Solution(object):
    def isMonotonic(self, nums):
        inc = dec = True
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                dec = False
            elif nums[i] > nums[i+1]:
                inc = False
        
        return inc or dec


        