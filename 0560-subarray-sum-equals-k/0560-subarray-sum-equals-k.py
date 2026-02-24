class Solution:
    def subarraySum(self, nums, k):
        curr_sum=0
        count=0
        prifix={0:1}
        for i in nums:
            curr_sum+=i
            if curr_sum-k in prifix:
                count+=prifix[curr_sum-k]
            prifix[curr_sum]=prifix.get(curr_sum,0)+1

        
        return count