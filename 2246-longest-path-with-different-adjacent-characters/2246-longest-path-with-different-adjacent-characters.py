class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj = defaultdict(list)
        for index, value in enumerate(parent):
            if(value != -1):
                adj[value] += [index]
        self.longest_path = 0
        def dfs(source):
            max1, max2 = 0,0
            for vertex in adj[source]:
                length = dfs(vertex)
                if(s[vertex] != s[source]):
                    if(length >= max1):
                        max2 = max1
                        max1 = length
                    elif(length > max2):
                        max2 = length
            self.longest_path = max(self.longest_path, max1 + max2 + 1)
            return max1 + 1
        dfs(0)
        return self.longest_path
