class Solution(object):
    def searchInsert(self,nums, target):
        n=len(nums)
        l=0
        h=n-1
        while l<=h:
            mid=(l+h)//2
            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                h=mid-1
            else:
                l=mid+1
        return l