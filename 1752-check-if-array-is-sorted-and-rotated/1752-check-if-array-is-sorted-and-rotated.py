class Solution:
    def check(self, nums: List[int]) -> bool:
        S=sorted(nums)
        for start in range(len(nums)):
            if nums[start: ] + nums[ :start] == S:
                return True
        return False 