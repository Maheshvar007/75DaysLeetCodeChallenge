class Solution(object):
    def checkInclusion(self, s1, s2):
        return any(sorted(s1) == sorted(s2[i:i+len(s1)]) for i in range(len(s2)-len(s1)+1))