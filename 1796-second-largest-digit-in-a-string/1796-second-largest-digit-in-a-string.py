class Solution:
    def secondHighest(self, s: str) -> int:
        dig=set()
        for i in s:
            if i.isdigit():
                dig.add(int(i))
        if len(dig)<2:
            return -1
        first=float('-inf')
        sec=float('-inf')

        for i in dig:
            if i > first:
                sec=first
                first=i
            if i<first and i > sec:
                sec=i
        if sec == float('-inf'):
            return -1
        return sec     