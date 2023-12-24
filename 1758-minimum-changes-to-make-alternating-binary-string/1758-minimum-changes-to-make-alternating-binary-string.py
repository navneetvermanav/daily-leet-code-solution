class Solution:
    def minOperations(self, s: str) -> int:
        cnt = 0 # "010101..."
        for i, c in enumerate(s): 
            if i&1 == int(c): cnt += 1
        return min(cnt, len(s) - cnt)