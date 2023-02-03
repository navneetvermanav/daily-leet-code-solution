class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        g = list(range(numRows)) + list(range(numRows - 2, 0, -1))
        l = [""] * numRows
        for i in range(len(s)):
            l[g[i % (numRows + numRows - 2)]] += s[i]
        return "".join(l)