class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        if R == C == 1:
            return 0
        
        def neighs(r, c):
            for nx, ny in ((r + 1, c), (r, c + 1), (r - 1, c),(r, c - 1)):
                if 0 <= nx < R and 0 <= ny < C:
                    yield nx, ny, abs(heights[r][c] - heights[nx][ny])
        
        INF = float("inf")
        dist_start = defaultdict(lambda: INF, {(0, 0): 0})
        dist_end = defaultdict(lambda: INF, {(R - 1, C - 1): 0})
        heap_start, heap_end = [(0,0,0)], [(0, R - 1, C - 1)]
        mu = INF
        while heap_start and heap_end:
            max_start, start_r, start_c = heappop(heap_start)
            max_end, end_r, end_c = heappop(heap_end)
            
            if max(max_start, max_end) >= mu:
                return mu
            
            for nx, ny, cost in neighs(start_r, start_c):
                if (candidate := max(max_start, cost)) < dist_start[(nx, ny)]:
                    dist_start[(nx, ny)] = candidate
                    heappush(heap_start, (candidate, nx, ny))

                if dist_end[(nx, ny)] != INF:
                    mu = min(mu, max(dist_start[(nx, ny)], dist_end[(nx, ny)]))
                            
            for nx, ny, cost in neighs(end_r, end_c):
                if (candidate := max(max_end, cost)) < dist_end[(nx, ny)]:
                    dist_end[(nx, ny)] = candidate
                    heappush(heap_end, (candidate, nx, ny))

                if dist_start[(nx, ny)] != INF:
                    mu = min(mu, max(dist_start[(nx, ny)], dist_end[(nx, ny)]))
        return -1