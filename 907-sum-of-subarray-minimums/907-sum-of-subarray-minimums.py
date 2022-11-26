class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [-1]
        result = 0
        for idx, x in enumerate(arr + [0]):
            while len(stack) > 1 and x < arr[stack[-1]]:
                index = stack.pop()
                left_length = index - stack[-1]
                right_length = idx - index
                result += left_length * right_length * arr[index]
            stack.append(idx)
        return result % (10 ** 9 + 7)
