class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        maxv=0
        v=set("aeiou")
        for i in range(k):
            if s[i] in v:
                count+=1
        maxv=count
        for i in range(k,len(s)):
            if s[i] in v:
                count+=1
            if s[i-k] in v:
                count-=1
            maxv=max(maxv,count)
        return maxv
        