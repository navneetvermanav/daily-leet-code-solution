class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		days = [0]*len(temperatures)
		stack = []
		for i in range(0,len(temperatures)):
			while stack and temperatures[stack[-1]] < temperatures[i]:
				last = stack.pop()
				days[last] = i-last
			stack.append(i)

		return days
