class Solution:
    def missingNumber(self, nums):
        n=len(nums)
        sumVal=(n*(n+1))//2
        total=0
        for i in nums:
            total+=i
        return (sumVal-total)