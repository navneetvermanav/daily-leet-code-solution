class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        right = len(nums) - 1
        left = 0
        square = [0] * (right + 1)
        while(right>=left):
            if(pow(nums[right],2) > pow(nums[left],2)):
                square[right-left] = pow(nums[right],2)
                right = right - 1
                continue
            if(pow(nums[right],2) <= pow(nums[left],2)):
                square[right-left] = pow(nums[left],2)
                left = left + 1
                continue
        return square