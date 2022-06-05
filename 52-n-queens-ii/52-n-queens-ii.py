class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        visited = [[0] * n for _ in range(n)]
        self.res = 0
        self.backtrack(visited,0)
        return self.res
    
    def sign(self,visited,x,y,s):
        tx = x
        ty = y
        while x < len(visited) and y < len(visited):
            visited[x][y] += s
            x += 1
            y += 1
        x = tx
        y = ty
        while tx < len(visited) and ty >= 0:
            visited[tx][ty] += s
            tx += 1
            ty -= 1
        while x < len(visited):
            visited[x][y] += s
            x += 1
    def backtrack(self,visited,x):
        if x == len(visited) - 1:
            self.res += visited[-1].count(0)
            return 
        for i in range(len(visited)):
            if visited[x][i] == 0:
                self.sign(visited,x,i,1)
                self.backtrack(visited,x + 1)
                self.sign(visited,x,i,-1)
               