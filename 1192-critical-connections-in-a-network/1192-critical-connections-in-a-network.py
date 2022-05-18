class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for e in connections:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
        visited = [False]*n  
        low = [math.inf]*n  
        ids = [-1] * n      
        id_counter = 0                  
        bridges = []         
        
        stack = []                
        
        def dfs(at: int, fr: int):
            nonlocal id_counter
            ids[at] = low[at] = id_counter
            id_counter += 1
            
            stack.append(at)
            visited[at] = True
            
            for to in graph[at]:           
                if to == fr:
                    continue     
                if ids[to] == -1:
                    dfs(to, at) 
                    if ids[at] < low[to]:
                        bridges.append([at, to]) 
                if visited[to]:
                    low[at] = min(low[at], low[to])
            
            if ids[at] == low[at]:
                node = stack.pop()
                while node:
                    visited[node] = False  
                    if node == at:
                        break
                    node = stack.pop()                
        
        for node in range(n):
            if ids[node] == -1:
                dfs(node, None)
        
        return bridges