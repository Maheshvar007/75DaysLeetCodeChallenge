class Solution:
    def decodeString(self, s):
        st, cur, num = [], "", 0
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)

            elif c == '[':
                st.append((cur, num))
                cur, num = "", 0
            elif c == ']':
                p, k = st.pop()
                cur = p + cur*k
            else:
                cur += c
        return cur