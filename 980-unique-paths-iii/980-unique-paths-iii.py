class Solution:
    def uniquePathsIII(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        start = end = p = 0 
        # Flatten the array for better performance
        A = reduce(operator.add, A)
        for key, val in enumerate(A):
            if val >= 0:
                p += 1 # Count the number of none obstacle square  
                if val == 1: start = key # get start and end index
                if val == 2: end = key
                    
        l = m*n 
        def dfs(i, p): 
            if i == end and not p: 
                return 1
            if A[i] < 0 or i == end: return 0
            A[i], res= -1, 0 # place an obstacle on the square when passing by
            
            # check every legal action
            if i >= n: res += dfs(i - n, p - 1)
            if i < l - n: res += dfs(i + n, p - 1)
            if i % n: res += dfs(i - 1, p - 1)
            if (i - n + 1) % n: res += dfs(i + 1, p - 1) 
            
            A[i] = 0 # backtrack, remove obstacle
            return res
        return dfs(start, p-1)
