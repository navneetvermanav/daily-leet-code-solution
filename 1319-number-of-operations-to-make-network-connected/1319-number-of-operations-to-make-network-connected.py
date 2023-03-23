from collections import deque

class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
        if len(connections) < n - 1:
            return -1
        
        cluster, queue, graph, visited = 0, deque([]), [[] for i in range(n)], set([])
        
        # Creating Graph
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])
            
        # Counting isolated clusters using BFS
        for i in range(n):
            if i not in visited:
                cluster += 1
                queue.append(i)
                visited.add(i)
                
                # BFS
                while queue:
                    node = queue.popleft()
                    
                    for nhbrs in graph[node]:
                        if nhbrs not in visited:
                            queue.append(nhbrs)
                            visited.add(nhbrs)
        
        # Counting Min number of times to get connections
        return (cluster - 1)