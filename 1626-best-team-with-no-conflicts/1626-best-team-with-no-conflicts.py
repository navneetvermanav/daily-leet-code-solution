class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        data=list(zip(ages,scores))
        data.sort()
        n=len(scores)
        dp=[0]*n
        
        for i in range(n):
            cur_scores=data[i][1]
            dp[i]=cur_scores
            
            for j in range(i):
                if data[j][1]<=cur_scores:
                    dp[i]=max(dp[i],dp[j]+cur_scores)
                    
        return max(dp)            