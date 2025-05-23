class Solution(object):
    def removeDuplicates(self, nums):
        list1=[]
        i=0
        while i<len(nums):
            if nums[i] not in list1:
                list1.append(nums[i])
                i+=1
            else:
                nums.pop(i)
        