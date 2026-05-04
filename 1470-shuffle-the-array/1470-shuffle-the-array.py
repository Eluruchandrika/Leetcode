class Solution:
    def shuffle(self, nums, n):
        res=[]
        i=0
        j=n
        while j < n*2:
            res.append(nums[i])
            res.append(nums[j])
            i=i+1
            j=j+1
        return res
        