class Solution(object):
    def minCostClimbingStairs(self, cost):
        a = b = 0
        for c in cost:
            a, b = b, c + min(a, b)
        return min(a, b)