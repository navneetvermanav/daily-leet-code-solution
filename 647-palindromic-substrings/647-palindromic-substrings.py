class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        count = 0
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        i = n -1
        while i >= 0:
            j = i
            while j < n:
                #substring length > = 2
                if j-i > 1:
                    #abca
                    if s[i] == s[j]:
                        if dp[i+1][j-1]:
                            dp[i][j] = True
                            count += 1
                        else:
                            dp[i][j] = False
                    else:
                        dp[i][j] = False
                        #aa
                elif j - i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        count += 1
                    else:
                        dp[i][j] = False
                        #a
                else:
                    dp[i][j] = True
                    count += 1
                j += 1
            i -= 1
        return count 