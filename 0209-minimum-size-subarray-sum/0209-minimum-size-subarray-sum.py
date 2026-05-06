class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        s = 0
        ans = float('inf')
        for right in range(len(nums)):
            s += nums[right]
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans