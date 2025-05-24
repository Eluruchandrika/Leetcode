class Solution(object):
    def sortColors(self, nums):
        l=0
        h=len(nums)-1
        m=0
        while m<=h:
            if nums[m]==0:
                nums[m],nums[l]=nums[l],nums[m]
                m+=1
                l+=1
            elif nums[m]==1:
                m+=1
            else:
                nums[m],nums[h]=nums[h],nums[m]
                h-=1
        return nums