class Solution:
    def calculate(self, expression: str) -> int:
        def helper(s,index):
            result = 0
            sign = 1
            currnum = 0
            i = index
            while i<len(s):
                c = s[i]
                if c.isdigit():
                    currnum = currnum*10+int(c)
                elif c in '-+':
                    result += sign*currnum
                    sign = 1 if c=='+' else -1
                    currnum = 0
                elif c == '(':
                    res, i = helper(s, i+1)
                    result += sign*res
                elif c == ')': 
                    result += sign*currnum
                    break
                i+=1
            return result, i
                
        if not expression:
            return 0
        return helper('('+expression+')', 0)[0]