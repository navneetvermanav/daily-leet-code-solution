class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # get vector of counts of all letters for subtree
        def dfs(node):
            count = Counter(labels[node])
            for child in graph[node]:
                # discard so no repeat
                graph[child].discard(node)

                # add characters of all subtrees
                count += dfs(child)

            ret[node] = count[labels[node]]
            return count
        # make graph of the tree
        graph = collections.defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
    
        ret = [0] * n
        dfs(0)
        return ret
