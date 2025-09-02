class Solution:
    def maxDepth(self, s: str) -> int:
        maxVal=0
        count=0
        for i in s:
            if i =="(":
                count+=1
            if i ==")":
                count-=1
            maxVal=max(count,maxVal)
        return maxVal
        