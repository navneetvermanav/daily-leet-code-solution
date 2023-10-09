class Solution:
    def maxDotProduct(self, nums1, nums2):
        M, N = len(nums1), len(nums2)
		
        if (max(nums1) < 0 and min(nums2) > 0):
            return max(nums1) * min(nums2) 
        if (max(nums2) < 0 and min(nums1) > 0):
            return min(nums1) * max(nums2)         
			
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for i in range(M):
            for j in range(N):
                dp[i+1][j+1] = max(dp[i][j] + nums1[i]*nums2[j], dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]