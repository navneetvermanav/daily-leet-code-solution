class Solution:
    def minimumLength(self, s):
        while len(s) > 1 and s[0] == s[-1]:
            s = s.strip(s[0])
        return len(s)
        