class Solution(object):
    def findDuplicates(self, nums):
        res = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                res.append(abs(nums[i]))
            else:
                nums[index] *= -1
        return res
