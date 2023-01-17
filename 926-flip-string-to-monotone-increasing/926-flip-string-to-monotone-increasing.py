class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        total = flip = 0
        for c in s:
            total += c == '1'
            if c == '0':
                flip = min(flip + 1, total)
        return flip
