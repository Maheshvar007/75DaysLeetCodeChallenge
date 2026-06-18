class Solution(object):
    def divide(self, dividend, divisor):
        q = int(float(dividend) / divisor)
        if q > 2**31 - 1:
            return 2**31 - 1
        if q < -2**31:
            return -2**31
        return q