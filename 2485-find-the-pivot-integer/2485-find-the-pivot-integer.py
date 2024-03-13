class Solution:
    def pivotInteger(self, n: int) -> int:
        
        x = bisect_right(range(n+1), 0, key=lambda x: (x+1)**2 - n*(n+1)//2)
        return x if x**2 == n*(n+1)//2 else -1