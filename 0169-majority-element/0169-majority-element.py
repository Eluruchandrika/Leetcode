class Solution(object):
    def majorityElement(self, nums):
        count =0
        candi = None

        for num in nums:
            if count ==0:
                candi = num
            count+=(1 if candi == num else -1)
        return candi
        