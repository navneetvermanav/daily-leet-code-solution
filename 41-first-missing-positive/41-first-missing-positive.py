class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		def swap(nums: List[int], i: int, j: int):
			tmp = nums[i]
			nums[i] = nums[j]
			nums[j] = tmp
		
		length = len(nums)
		for index in range(len(nums)):
			while( nums[index] > 0 and nums[index] <= length and nums[nums[index] - 1] != nums[index]):
				swap(nums, index, nums[index] - 1)
				
		for index in range(len(nums)):
			if nums[index] != index + 1: return index + 1
		return length + 1
