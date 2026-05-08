class Solution(object):
    def checkInclusion(self, s1, s2):
        from collections import Counter
        n = len(s1)
        target = Counter(s1)
        for i in range(len(s2) - n + 1):
            if Counter(s2[i:i+n]) == target:
                return True
        return False