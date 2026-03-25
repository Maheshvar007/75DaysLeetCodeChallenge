class Solution(object):
    def maxProfit(self,prices):
        mn = prices[0]
        profit = 0
        for p in prices:
            mn = min(mn, p)
            profit = max(profit, p - mn)
        return profit
