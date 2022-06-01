class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        return [s:=s+v for _, v in enumerate(nums)]