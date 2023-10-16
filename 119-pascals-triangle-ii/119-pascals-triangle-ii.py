class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        s = 1
        res = [s]
        for i in range(rowIndex):
            s = s * (rowIndex-i) // (i+1)
            res.append(s)
        return res