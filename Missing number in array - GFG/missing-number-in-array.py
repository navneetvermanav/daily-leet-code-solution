#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        # code here
        '''
        a=[]
        sum1=0
        sum2=0 
        
        array.sort()
        for i in range (1,n+1):
            if i not in array:
                return i 
        return 0
        
        for i in array:
            sum1=sum1+i
            return sum1
        for j in  n:
            sum2=sum2+j
            return sum2
        return (sum2-sum1)
        '''
        return list(set(range(1,n+1)) - set(array))[0]
        
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends