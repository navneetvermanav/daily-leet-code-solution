class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        currSum, maxSum = nums[0], nums[0]
        visited = set([nums[0]])
        
        for right in range(1, len(nums)):
            if nums[right] in visited:
                while nums[right] != nums[left]:
                    currSum -= nums[left]
                    visited.remove(nums[left])
                    left += 1
                currSum -= nums[left]
                visited.remove(nums[left])
                left += 1
                
            visited.add(nums[right])
            currSum += nums[right]
            maxSum = max(currSum, maxSum)
            
        return maxSum