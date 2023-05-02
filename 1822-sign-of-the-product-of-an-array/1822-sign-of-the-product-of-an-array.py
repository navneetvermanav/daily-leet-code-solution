class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        else:
            cnt=1
            for i in nums:
                cnt *= i
            if cnt > 0:
                return 1
            else:
                return -1