class Solution(object):
    def majorityElement(self, nums):
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        for i,j in count.items():
            if j>len(nums)//2:
                return i 