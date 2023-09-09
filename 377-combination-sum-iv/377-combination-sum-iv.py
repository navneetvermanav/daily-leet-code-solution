class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def helper(t, memo): # Base case
            if t == 0:
                return 1
            if memo[t] != -float("inf"): # memorization kicks in
                return memo[t]
            else:
                res = 0
                for i in range(len(nums)):
                    if t - nums[i] >= 0: # discard the negative states
                        res += helper(t - nums[i], memo)
                memo[t] = res # memorize the total number off this branch
                return memo[t]

        memo = [-float("inf") for _ in range(target+1)]
        memo[0] = 1
        return helper(target, memo)