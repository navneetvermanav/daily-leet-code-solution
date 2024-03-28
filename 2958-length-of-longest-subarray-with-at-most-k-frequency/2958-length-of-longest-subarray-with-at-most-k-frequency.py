class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        ans = ii = 0
        for i, x in enumerate(nums): 
            freq[x] += 1
            while freq[x] > k: 
                freq[nums[ii]] -= 1
                ii += 1
            ans = max(ans, i-ii+1)
        return ans 