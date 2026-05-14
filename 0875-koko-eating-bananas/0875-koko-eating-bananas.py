class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if sum((p + m - 1) // m for p in piles) <= h:
                r = m
            else:
                l = m + 1
        return l