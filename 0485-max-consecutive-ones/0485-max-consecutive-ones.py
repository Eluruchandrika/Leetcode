class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxx=0
        curr=0
        for i in nums:
            if i ==1:
                curr+=1
            else:
                maxx=max(curr,maxx)
                curr=0
        maxx=max(curr,maxx)
        return maxx
        