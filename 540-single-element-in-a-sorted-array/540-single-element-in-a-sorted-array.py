class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def helper():
            xor = 0
            for i in nums:
                xor ^= i
            return xor
        return helper()



        