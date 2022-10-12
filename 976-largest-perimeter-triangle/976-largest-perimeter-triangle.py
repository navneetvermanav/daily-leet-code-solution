class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        for i in range(0, len(nums) - 2):
            a, b, c = nums[i:i+3]
            if (a < b + c) and (b < a + c) and (c < a + b):
                return a + b + c
        return 0
        