class Solution(object):
    def moveZeroes(self, nums):
        first=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[first]=nums[first],nums[i]
                first+=1
        return nums


        
        