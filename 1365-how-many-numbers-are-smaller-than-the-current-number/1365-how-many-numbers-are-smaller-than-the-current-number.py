class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums=sorted(nums)
        dic={}
        for i,num in enumerate(sorted_nums):
            if num not in dic:
                dic[num]=i
        return [dic[i] for i in nums]
        