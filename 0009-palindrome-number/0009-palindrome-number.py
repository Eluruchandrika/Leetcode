class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        dup=x
        res=0
        x=abs(x)
        while x>0:
            ld=x%10
            res=res*10+ld
            x=x//10
        return res==dup
        

        
        