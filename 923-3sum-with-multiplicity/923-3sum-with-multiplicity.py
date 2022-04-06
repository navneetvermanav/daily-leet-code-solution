class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
   
        mem = {}
        def rec(idx, t, iteration):
            key = str(idx) + '-' + str(t) + '-' + str(iteration)
            if key in mem: return mem[key]
            if t == 0 and iteration == 0:

                return 1
            if idx < 0 or iteration <= 0 or t < 0: return 0
            x = arr[idx]
            pos1 = rec(idx-1, t-x, iteration-1)
            pos2 = rec(idx-1, t, iteration)
            
     
            mem[key] = pos1 + pos2
            return mem[key]
        return rec(len(arr)-1, target, 3) % (10**9 + 7)