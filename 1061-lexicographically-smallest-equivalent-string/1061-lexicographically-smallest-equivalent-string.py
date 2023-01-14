class UnionFind:
    def __init__(self):
        self.data = {chr(ord('a') + i):chr(ord('a') + i) for i in range(26)}

    def find(self, c):
        if c != self.data[c]:
            self.data[c] = self.find(self.data[c])
        return self.data[c]
    
    def union(self, a, b):
        if a == b: return
        x = self.find(a)
        y = self.find(b)
        if x < y: self.data[y] = x
        else: self.data[x] = y

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for i in range(len(s1)): uf.union(s1[i], s2[i])
        return ''.join([ uf.find(c) for c in baseStr ])
