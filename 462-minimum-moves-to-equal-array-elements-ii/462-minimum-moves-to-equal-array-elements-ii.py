class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        target=nums[n//2]
        return sum(abs(target-n)for n in nums)