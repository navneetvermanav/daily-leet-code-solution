class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        l=[[] for _ in range(n)]
        for i,j in edges: l[i].append(j), l[j].append(i)
        @lru_cache(None)
        def dp(i, prev):
            res, c = 0, 1
            for j in l[i]:
                if j==prev: continue
                v = dp(j, i)
                res, c = res + v[0] + v[1], c + v[1]
            return (res, c)
        return [dp(i,i)[0] for i in range(n)]
