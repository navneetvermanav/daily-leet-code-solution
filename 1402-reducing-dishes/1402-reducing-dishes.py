class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        sat = sorted(sat)
        
        sm, res , idx , nend = 0,0,1,-1
        for i in range(0,len(sat)):
            if(sat[i] >= 0 ):
                sm += sat[i]
                res += sat[i]*idx 
                idx += 1
            if(i>0 and sat[i] >= 0 and sat[i-1] < 0 ):
                nend = i-1 ; 
        
        while nend >=0 :
            if( res+sm+sat[nend] > res ):
                res = res+sm+sat[nend]
                sm = sm + sat[nend]
                nend -= 1
            else:
                break;
        return res
