class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		# initially all are 0
		days = [0]*len(temperatures)
		stack = []

		# keep a stack, which tracks max elements from bottom to top
		for i in range(0,len(temperatures)):
			# if we find a smaller element on the top of the stack, we pop it and then calculate the distance
			while stack and temperatures[stack[-1]] < temperatures[i]:
				last = stack.pop()
				days[last] = i-last
			stack.append(i)

		return days
