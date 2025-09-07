class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i=0
        res=[]
        while i < len(nums1):
            j=0
            num=False
            while j < len(nums2):
                if nums2[j] == nums1[i]:
                    num=True
                if num and nums2[j]>nums1[i]:
                    res.append(nums2[j])
                    num=False
                    break
                j=j+1
            if num==True:
                res.append(-1)
            i=i+1
        return res
        