class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        p = 0
        q = 0

        while p < s_len and q < t_len:
            if s[p] == t[q]:
                 p += 1
            q += 1
        return p == s_len
