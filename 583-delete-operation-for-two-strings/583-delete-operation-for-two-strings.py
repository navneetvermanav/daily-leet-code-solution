from collections import defaultdict

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M = len(word1)
        N = len(word2)
        
        memo = defaultdict(int)
        longest_common_subsequence_len = self.helper(0, word1, M, 0, word2, N, memo)
        return (M + N) - (2 * longest_common_subsequence_len)
    
    def helper(self, i, A, M, j, B, N, memo):
        if (i,j) in memo:
            return memo[(i,j)]
        
        if i >= M or j >= N:
            return 0
        
        answer = -1
        if A[i] == B[j]:
            answer = 1 + self.helper(i + 1, A, M, j + 1, B, N, memo)
        else:
            answer = max(self.helper(i, A, M, j + 1, B, N, memo),
                      self.helper(i + 1, A, M, j, B, N, memo))
        
        memo[(i,j)] = answer
        return answer
        

# Bottom-Up DP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M = len(word1) + 1
        N = len(word2) + 1
        
        dp = [[0] * M for _ in range(N)]
        
        for i in range(1, N):
            for j in range(1, M):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return (M + N - 2) - (2 * dp[-1][-1])