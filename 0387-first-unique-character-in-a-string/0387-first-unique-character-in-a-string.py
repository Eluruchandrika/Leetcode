class Solution:
    def firstUniqChar(self, s: str) -> int:

        charCount = {}

        for i in s:
            charCount[i] = charCount.get(i,0) +1
        
        for i in range(len(s)):
            if charCount[s[i]] == 1:
                return i
        return -1
        