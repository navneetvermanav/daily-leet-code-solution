class Solution:
    def maxScore(self, s: str) -> int:
        zeros, accu, ones, score = 0, 0, 0, 0
        for i in range(1, len(s) - 1):
            if s[i] == '1':
                ones += 1
                accu -= 1
            else:
                zeros += 1
            score = max(score, zeros + accu)
        return score + ones + (s[0] == '0') + (s[-1] == '1')