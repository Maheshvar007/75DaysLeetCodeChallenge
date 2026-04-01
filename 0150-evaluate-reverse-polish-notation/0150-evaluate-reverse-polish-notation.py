class Solution(object):
    def evalRPN(self, tokens):
        s=[]
        for t in tokens:
            if t not in "+-*/":
                s.append(int(t))
            else:
                b,a=s.pop(),s.pop()
                if t=='+': s.append(a+b)
                elif t=='-': s.append(a-b)
                elif t=='*': s.append(a*b)
                else: s.append(int(float(a)/b))
        return s.pop()