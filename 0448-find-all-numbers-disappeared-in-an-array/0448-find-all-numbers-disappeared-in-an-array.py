class Solution(object):
    def findDisappearedNumbers(self, nums):
        n=len(nums)
        return list(set(range(1,n+1))-set(nums))
        