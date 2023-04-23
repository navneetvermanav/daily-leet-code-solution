class Solution(object):
    def numberOfArrays(self, s, k):
        n=len(s)
        new=[0]*n
        new[0]=1
        m=len(str(k))
        for i in range(1,n):
            for j in range(max(0,i-m+1),i+1):
                if s[j]!="0" and int(s[j:i+1])<=k:
                    if j==0:
                        new[i]=1
                    else:
                        new[i]+=new[j-1]
                #print(new)
        
        return new[-1]%(10**9+7)