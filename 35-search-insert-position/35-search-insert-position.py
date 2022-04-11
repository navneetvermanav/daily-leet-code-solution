class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target < nums[0]: return 0
        if target > nums[len(nums)-1]: return len(nums)
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            
        for i in range(1,len(nums)):
            if target > nums[i-1] and target < nums[i]:
                return i
        
    def searchInsert1(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while(start<=end):
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start