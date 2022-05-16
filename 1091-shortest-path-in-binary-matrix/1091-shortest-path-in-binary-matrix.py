class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        n = len(grid)
        q = [[1,0,0]]
        grid[0][0] = 1
        
        while q:
            cost,x,y = heapq.heappop(q)
            
            if x==n-1 and y==n-1:
                return cost
            
            for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                if 0<=x+dx<n and 0<=y+dy<n and not grid[x+dx][y+dy]:
                    grid[x+dx][y+dy] = 1
                    heapq.heappush(q,[cost+1,x+dx,y+dy])
        
        return -1