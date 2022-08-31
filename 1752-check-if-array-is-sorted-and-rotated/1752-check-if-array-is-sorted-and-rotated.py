class Solution:
    def check(self, nums: List[int]) -> bool:
        Sorted = sorted(nums)
        for start in range(len(nums)):
            if nums[start: ] + nums[ :start] == Sorted:
                return True
        return False 