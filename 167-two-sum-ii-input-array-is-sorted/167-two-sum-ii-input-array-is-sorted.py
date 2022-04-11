class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            index=bisect.bisect_right(nums[0:i:],target-nums[i])
            if index!=0 and (nums[index-1]+nums[i])==target:
                return [index,i+1]
        return []