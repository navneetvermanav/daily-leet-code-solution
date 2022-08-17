class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        dp_max = [0]*N
        dp_min = [0]*N
        
        dp_max[0] = dp_min[0] = nums[0]
        for i in range(1,N):
            dp_max[i] = max(nums[i]*dp_max[i-1],nums[i],dp_min[i-1]*nums[i])
            dp_min[i] = min(nums[i]*dp_min[i-1],nums[i],dp_max[i-1]*nums[i])
        maxes = [0]*N
        
        for i in range(N):
            maxes[i] = max(dp_max[i],dp_min[i])
            
        return max(maxes)