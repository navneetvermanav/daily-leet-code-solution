class Solution:
	def checkSubarraySum(self, nums: List[int], k: int) -> bool:
		res = {0: -1}
		prefSum = 0
		for i in range(len(nums)):
			prefSum += nums[i]
			rem = prefSum % k
			if rem in res:
				if i-res[rem] > 1:
					return True
			else:
				res[rem] = i
		return False