class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        left=0
        curr=1
        count=0
        for right in range(len(nums)):
            curr*=nums[right]
            while curr>=k and left<=right:
                curr=curr//nums[left]
                left+=1
            if curr<k:
                count+=right-left+1
        return count

        