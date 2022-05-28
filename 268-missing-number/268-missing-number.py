class Solution:
	def missingNumber(self, nums: List[int]) -> int:

		l = len(nums)

		total_sum = l*(l+1)//2

		result = total_sum - sum(nums)

		return result