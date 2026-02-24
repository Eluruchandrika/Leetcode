class Solution:
    def lengthOfLongestSubstring(self, s):
        chSet=set()
        l=0
        maxLen=0
        for r in s:
            while r in chSet:
                chSet.remove(s[l])
                l+=1
            chSet.add(r)
            maxLen=max(maxLen,len(chSet))
        return maxLen
        