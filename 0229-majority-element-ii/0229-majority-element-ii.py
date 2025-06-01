class Solution(object):
    def majorityElement(self, nums):
        
        n=len(nums)
        count1=count2=0
        candi1=candi2=None

        for num in nums:
            if candi1 == num:
                count1+=1
            elif candi2 == num:
                count2+=1
            elif count1 == 0:
                candi1 = num
                count1=1
            elif count2 == 0:
                candi2 = num
                count2 = 1
            else:
                count1-=1
                count2-=1
                
        res=[]
        
        for i in [candi1,candi2]:
            if nums.count(i)> n/3:
                res.append(i)

        return sorted(res)

        