class Solution:
    def bitCount(self,n):
        count = 0
        while n != 0:
            n = n&(n-1)
            count += 1
        return count
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        d = {}
        for i in arr:
            numBit = self.bitCount(i)
            if numBit in d:
                arr = d[numBit]
                arr.append(i)
                d[numBit] = arr
            else:
                d[numBit] = [i]
                val = []
        for i in d:
            val.append(i)
        val.sort()
        ans = []
        for i in val:
            for j in d[i]:
                ans.append(j)
        return ans