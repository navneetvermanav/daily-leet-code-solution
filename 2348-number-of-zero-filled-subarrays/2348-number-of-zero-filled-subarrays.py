class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        currPool = 0
        for n in nums:
            if n == 0:
                currPool += 1
            elif currPool > 0:
                ans += int((currPool * (currPool + 1))/2)
                currPool = 0
        
        ans += int((currPool * (currPool + 1))/2)
        return ans