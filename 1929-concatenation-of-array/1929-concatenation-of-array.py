class Solution:
    def getConcatenation(self, nums):
        l=len(nums)
        ans_len=l*2
        ans=[0]*ans_len
        for i in range(l):
            ans[i]=nums[i]
            ans[i+l]=nums[i]
        return ans
        