class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        ans = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                H = heights[stack.pop()]
                W = i if not stack else i - stack[-1] - 1
                ans = max(ans, H * W)
            stack.append(i)
        return ans