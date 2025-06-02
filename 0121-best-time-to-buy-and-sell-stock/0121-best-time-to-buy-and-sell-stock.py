class Solution:
    def maxProfit(self, prices):
        minprice= float("inf")
        profit =0
        for i in prices:
            if i < minprice:
                minprice = i
            if i - minprice > profit:
                profit=i - minprice
        return profit
        