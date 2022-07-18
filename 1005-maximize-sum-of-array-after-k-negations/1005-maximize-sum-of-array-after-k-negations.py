class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        if nums[-1] < 0: # all negative
            idx = 0
            while idx < len(nums):
                nums[idx] = -nums[idx]
                idx += 1
                k -= 1
                if k == 0:
                    break
            if k > 0:
                if k % 2 == 1:
                    nums[-1] = -nums[-1]
        elif nums[0] > 0: 
            if k % 2 == 1:
                nums[0] = -nums[0]
        else: # mix
            idx = 0
            while idx < len(nums):
                if nums[idx] < 0:
                    nums[idx] = -nums[idx]
                    idx += 1
                    k -= 1
                    if k == 0:
                        break
                else:
                    if k % 2 == 1:
                        if idx > 0:
                            if nums[idx-1] < nums[idx]:
                                nums[idx-1] = -nums[idx-1]
                            else:
                                nums[idx] = -nums[idx]   
                    break
        return sum(nums)