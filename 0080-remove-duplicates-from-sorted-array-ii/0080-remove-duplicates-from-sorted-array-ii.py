class Solution(object):
    def removeDuplicates(self, nums):
        i=1
        curr=nums[0]
        count=1
        while i< len(nums):
            if nums[i] == curr:
                if count<2:
                    count+=1
                    i+=1
                else:
                    nums.pop(i)
            else:
                curr = nums[i]
                count=1
                i+=1


        
        