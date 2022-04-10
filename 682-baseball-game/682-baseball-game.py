class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for i in ops:
            if i == 'C':
                res.pop()
            elif i == 'D':
                res.append(res[-1] * 2)
            elif i == "+":
                res.append(res[len(res)-2] + res[-1])             
            else:
                res.append(int(i))
        return sum(res)