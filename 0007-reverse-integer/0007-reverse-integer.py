class Solution:
    def reverse(self, x: int) -> int:
        res=0
        temp=abs(x)
        while temp>0:
            last=temp%10
            res=res*10+last
            temp=temp//10
        
        if res>(2**31)-1 or res<(-2**31):
            return 0
        if x<0:
            return -res
        else:
          return res
        
        