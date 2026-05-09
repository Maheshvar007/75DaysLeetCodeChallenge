class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        return [next((y for y in nums2[nums2.index(x)+1:] if y>x), -1) for x in nums1]