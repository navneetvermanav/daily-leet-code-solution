class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ht = defaultdict(list)
        for i,j,dis in roads:
            ht[i].append(j)
            ht[j].append(i)
        ans,view= inf,set()
        queue = deque([1])
        while queue:
            cur_city = queue.popleft()
            for next_city in ht[cur_city]:
                if next_city not in view:
                    queue.append(next_city)
                    view.add(next_city)
        for i,j,dis in roads:
            if i in view or j in view:
                ans=min(ans,dis)
        return ans