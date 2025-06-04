class Solution:
    def addBinary(self, a: str, b: str) -> str:

        total = int(a, 2) + int(b, 2)
        if total == 0:
            return '0'

        result = ''
        while total > 0:
            rem = total % 2
            result = str(rem) + result
            total //= 2
            
        return result