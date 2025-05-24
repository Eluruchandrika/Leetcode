class Solution(object):
    def maximumWealth(self, accounts):
        res=0
        for i in accounts:
            curr=sum(i)
            if curr>res:
                res=curr
        return res


        