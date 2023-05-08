class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        
        mat_length = len(mat)
        mid = mat_length // 2
              
        i = 0
        j = mat_length - 1
        while i < mid:
            total += mat[i][i] + mat[i][j] + mat[j][i] + mat[j][j]
            i += 1
            j -= 1            
        
        if mat_length % 2 != 0:
            total += mat[mid][mid]
            
        return total