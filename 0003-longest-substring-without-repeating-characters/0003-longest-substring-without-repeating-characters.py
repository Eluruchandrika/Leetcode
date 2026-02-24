class Solution:
    def lengthOfLongestSubstring(self, s):
        chSet=[]
        maxLen=0
        for r in s:
            while r in chSet:
                chSet.pop(0)
            chSet.append(r)
            maxLen=max(maxLen,len(chSet))
        return maxLen
        