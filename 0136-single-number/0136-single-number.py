class Solution:
    def singleNumber(self, nums):
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for i,j in dic.items():
            if j==1:
                return i
        