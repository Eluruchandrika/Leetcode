class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        for i in s:
            if i =="(" or i=="[" or i == "{":
                arr.append(i)
            else:
                if len(arr) ==0:
                    return False
                ch=arr[-1]
                arr.pop()
                if (i==")" and ch=="(") or (i=="]" and ch=="[") or (i=="}" and ch=="{"):
                    continue
                else:
                    return False
        return len(arr)==0
        