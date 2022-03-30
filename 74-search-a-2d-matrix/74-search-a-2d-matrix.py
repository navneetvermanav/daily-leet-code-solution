class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        x = 0
        y = len(matrix) - 1
        while (x < y):
            row = x + (y - x) // 2
            if matrix[row][len(matrix[0]) - 1] >= target: y = row 
            else: x = row + 1
        row = x 
        
        x, y = 0, len(matrix[0]) - 1
        while (x <= y):
            col = x + (y - x) // 2
            if matrix[row][col] == target: return True
            if matrix[row][col] > target: y = col - 1
            else: x = col + 1
        return False