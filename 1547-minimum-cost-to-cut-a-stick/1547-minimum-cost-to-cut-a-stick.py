class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}
        def f(piece_begin, piece_end, c_i, c_j):
            if c_i > c_j or piece_begin + 1 >= piece_end:
                return 0
            if (piece_begin, piece_end, c_i, c_i) in memo:
                return memo[(piece_begin, piece_end, c_i, c_i)]
            
            min_cost = float('inf')
            for k in range(c_i, c_j + 1):
                loc = cuts[k]
                cost = f(piece_begin, loc, c_i, k-1) + f(loc, piece_end, k+1, c_j) + (piece_end - piece_begin)
                min_cost = min(min_cost, cost)
            memo[(piece_begin, piece_end, c_i, c_i)] = min_cost
            return memo[(piece_begin, piece_end, c_i, c_i)]
                
        cuts.sort()
        return f(0, n, 0, len(cuts) - 1)
