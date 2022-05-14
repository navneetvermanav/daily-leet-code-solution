class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = collections.defaultdict(list)
        
        # build graph
        for src, dst, weight in times:
            g[src].append((dst, weight))
        
        # k - node, v - weight (src to k)
        node2ws = {i: float('inf') for i in range(1, n + 1)}
        
        def dfs(source, cur_weight):
            if cur_weight < node2ws[source]:
                node2ws[source] = cur_weight
                
                for neigb, w in g[source]:
                    dfs(neigb, cur_weight + w)
        
        dfs(k, 0)
        
        ws = node2ws.values()
        
        _max = max(ws)
        
        return _max if _max != float('inf') else -1