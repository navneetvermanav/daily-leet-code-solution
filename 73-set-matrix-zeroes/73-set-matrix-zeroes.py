class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        checkr = {""}
        checkc = {""}
        
        n = len(mat)
        m = len(mat[0])
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    checkr.add(i)
                    checkc.add(j)
        
        for i in range(n):
            if i in checkr:
                mat[i] = [0]*m
                continue
            
            for j in range(m):
                if j in checkc:
                    mat[i][j] = 0