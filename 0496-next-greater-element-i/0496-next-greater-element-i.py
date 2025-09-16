class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res={}
        stack=[]

        for i in reversed(nums2):
            while stack and stack[-1]<i:
                stack.pop()
            res[i]=stack[-1] if stack else -1
            stack.append(i)
        
        return [res[i] for i in nums1]


            
