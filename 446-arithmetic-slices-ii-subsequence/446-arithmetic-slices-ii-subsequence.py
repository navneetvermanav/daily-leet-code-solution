class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        
        n = len(nums)
        dp = [{} for _ in range(n)]
        res = 0
        for i in range(1, n):
            for j in range(i):
                dif = nums[i] - nums[j]
                total = 0
                if dif in dp[j]:
                    total = dp[j][dif]
                if dif in dp[i]:
                    dp[i][dif] += total + 1
                else:
                    dp[i][dif] = total + 1
                res += total
        return res