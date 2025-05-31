class Solution(object):
    def findDuplicates(self, nums):
        arr = [0]*(len(nums)+1)
        res = []
        for num in nums:
            if(arr[num]>0):
                res.append(num)
            else:
                arr[num]=1
        return res
