class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        charCount = {}

        for i in s:
            charCount[i] = charCount.get(i,0)+1
        
        for i in t:
            charCount[i] = charCount.get(i,0)-1

        for val in charCount.values():
            if val !=0:
                return False
        
        return True

        