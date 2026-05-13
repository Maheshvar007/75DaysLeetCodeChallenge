class Solution(object):
    def findPeakElement(self, nums):
        p=max(nums)
        return nums.index(p)