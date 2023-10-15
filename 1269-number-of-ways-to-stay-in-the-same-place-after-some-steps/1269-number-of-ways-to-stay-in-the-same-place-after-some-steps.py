class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @lru_cache(None)
        def dfs(cur=0, s=steps):
            if not cur and not s: return 1
            if cur < 0 or cur == arrLen or s < 0: return 0
            return dfs(cur+1, s-1) + dfs(cur-1, s-1) + dfs(cur, s-1)
        
        return dfs() % int(1e9 + 7)