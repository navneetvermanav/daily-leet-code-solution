from collections import defaultdict
class DSU:
	def __init__(self,n):
		self.parent=[i for i in range(n+1)]
	def findPar(self,u):
		if self.parent[u]!=u:
			self.parent[u]=self.findPar(self.parent[u])
		return self.parent[u]
	def union(self,u,v):
		pu = self.findPar(u)
		pv = self.findPar(v)
		self.parent[pu] = pv

class Solution(object):
	def possibleBipartition(self, n, dislikes):
		dsu = DSU(n)
		adj=defaultdict(list)
		for i,j in dislikes:
			adj[i-1].append(j-1)
			adj[j-1].append(i-1)
		for i in range(n):
			nei = adj[i]
			dis = dsu.findPar(i)
			if not nei: continue
			for j in nei[1:]:
				if dsu.findPar(j)==dis:
					return False
				dsu.union(nei[0],j)
		return True
