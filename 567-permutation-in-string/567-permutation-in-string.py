class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        m = {}
        count = 0
        for c in s1:
            if c in m:
                m[c]+=1
            else:
                m[c]=1
                count+=1

        i = 0
        j = 0
        while j<len(s2):
            c = s2[j]
           
            if c in m:
                m[c]-=1
               
                if m[c] == 0:
                    count-=1
                    if count == 0:
                        return True
              
                elif m[c] == -1:
                    while m[c] < 0:
                        m[s2[i]]+=1
                        if m[s2[i]] == 1:
                            count+=1 # For s2[i]
                        i+=1
                j+=1
         
            else:
                for x in range(i,j):
                    m[s2[x]]+=1
                    if m[s2[x]] == 1:
                        count+=1
                j+=1
                i=j
                
        return False