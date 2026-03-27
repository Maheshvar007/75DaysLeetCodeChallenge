class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        left = ans = 0
        for i, c in enumerate(s):
            if c in seen and seen[c] >= left:
                left = seen[c] + 1
            seen[c] = i
            ans = max(ans, i - left + 1)
        return ans