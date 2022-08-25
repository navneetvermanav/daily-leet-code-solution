class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(mat)
        cols = len(mat[0])

        B0 = C0 = False
        for ci in range(0, cols):
            if mat[0][ci] == 0:
                B0 = True
        for ri in range(0, rows):
            if mat[ri][0] == 0:
                C0 = True
        for ri in range(1, rows):
            for ci in range(1, cols):
                if mat[ri][ci] == 0:
                    mat[0][ci] = 0
                    mat[ri][0] = 0
        for ri in range(1, rows):
            for ci in range(1, cols):
                if mat[0][ci] == 0 or mat[ri][0] == 0:
                    mat[ri][ci] = 0
                        
        if B0: 
            for ci in range(cols):
                mat[0][ci] = 0
        if C0: 
            for ri in range(rows):
                mat[ri][0] = 0