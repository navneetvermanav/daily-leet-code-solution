class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic = {}
        ct = 0
        for i in mat:
            dic[ct] =  i.count(1)
            ct += 1
        ans = []    
        while k != 0:
            mx = min(dic.values())
            
            for i in dic.keys():
                if dic[i] == mx:
                    ans.append(i)
                    del dic[i]
                    break
            k -= 1
            
        return ans