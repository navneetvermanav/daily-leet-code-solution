from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = [[0] * 3 for _ in range(len(nums) // 3)]

        index = 0
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] <= k:
                ans[index][2] = nums[i + 2]
                ans[index][0] = nums[i]
                ans[index][1] = nums[i + 1]
                index += 1
            else:
                return []

        return ans