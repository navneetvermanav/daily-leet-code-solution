class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        l = count = res = s = 0
        for r, i in enumerate(A):
            s += i
            if i == 1:
                count = 0
            while l<= r and s >= S:
                if s == S:
                    count += 1
                s -= A[l]
                l += 1
            res += count
        return res