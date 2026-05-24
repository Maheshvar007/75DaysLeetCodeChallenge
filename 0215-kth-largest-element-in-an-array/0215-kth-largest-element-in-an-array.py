'''import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
'''
class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k-1]