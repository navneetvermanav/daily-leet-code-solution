class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        if (k := k%(m*n)) == 0:
            return grid
        div = gcd(m*n, k)  
        for i in range(div):
            r, c = divmod(i, n)
            curr = grid[r][c]
            for j in range(m*n//div):
                r, c = divmod((i+k*(j+1))%(m*n), n)
                grid[r][c], curr = curr, grid[r][c]
        return grid