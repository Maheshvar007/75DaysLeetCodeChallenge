class Solution(object):
    def moveZeroes(self,nums): 
        nums[:]=[i for i in nums if i != 0] + [0]*nums.count(0)