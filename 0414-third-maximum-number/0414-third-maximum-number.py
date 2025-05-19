class Solution(object):
    def thirdMax(self, nums):
        max1=None
        max2=None
        max3=None
        for i in nums:
            if i > max1:
                max3=max2
                max2=max1
                max1=i
            elif i<max1 and i>max2:
                max3=max2
                max2=i
            elif i<max2 and i >max3:
                max3=i
        if max3!=None:
            return max3
        else:
            return max1
    