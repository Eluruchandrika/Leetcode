from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commen = strs[0]
        
        for i in strs[1:]:
            p1 = 0
            p2 = 0
            curr = ""
            
            while p1 < len(commen) and p2 < len(i):
                if commen[p1] == i[p2]:
                    curr += i[p2]
                    p1 += 1
                    p2 += 1
                else:
                    break
            
            commen = curr
            if not commen: 
                return ""
        
        return commen
