class Solution(object):
    def dominantIndex(self, nums):
        max1=max(nums)
        index=nums.index(max1)
        for i in nums:
            if i == max1:
                continue
            elif i*2>max1:
                return -1
        return index

        