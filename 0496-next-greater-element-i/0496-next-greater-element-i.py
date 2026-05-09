class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        st, d = [], {}
        for n in nums2:
            while st and st[-1] < n:
                d[st.pop()] = n
            st.append(n)
        return [d.get(x, -1) for x in nums1]