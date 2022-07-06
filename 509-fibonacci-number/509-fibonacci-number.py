class Solution:
    def fib(self, n: int) -> int:
        dc = {
            0 : 0,
            1 : 1
        }
        for x in range(2, n+1):
            if x not in dc:
                dc[x] = dc[x-1] + dc[x-2]
        
        return dc[n]