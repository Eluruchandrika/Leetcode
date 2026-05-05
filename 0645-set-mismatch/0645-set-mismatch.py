class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        freq=[0]*(n+1)
        for i in nums:
            freq[i]+=1
        rep=-1
        missing=-1
        for i in range(1,n+1):
            if freq[i]==2:
                rep=i
            if freq[i]==0:
                missing=i
        return [rep,missing]

        