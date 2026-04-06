class Solution(object):
    def findMin(self,nums):
        n=len(nums)
        snums=sorted(nums)
        return snums[0]