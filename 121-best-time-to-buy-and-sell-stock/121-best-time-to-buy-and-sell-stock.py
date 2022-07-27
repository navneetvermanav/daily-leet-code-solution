class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        min_left = [0] * n
        min_left[0] = prices[0]
        for i in range(1, n):
            min_left[i] = min(min_left[i-1], prices[i])
        
        max_diff = prices[-1] - min_left[-1]
        for i in range(n-2, -1, -1):
            if prices[i] - min_left[i] > max_diff:
                max_diff = prices[i] - min_left[i]
        return max_diff