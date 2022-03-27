class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = float('inf')
        res = 0
        for p in prices:
            profit = p - min_so_far 
            res = max(res, profit) 
            min_so_far = min(min_so_far, p) 
        return res
        