#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        count=0
        arr.sort()
        for i in range(len(arr)-2):
            first=arr[i]
            x=i+1  
            y=len(arr)-1
            while x<y:
                sm=arr[x]+arr[y]
                if sm+first==0:
                    count=count+1
                    return count
                    # answer.append((i,arr[x],arr[y]))
                    # print len(answer)
                elif sm+first>0:
                    y-=1
                elif sm+first<0:
                    x+=1
        return count
                    
        
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        if(Solution().findTriplets(a,n)):
            print(1)
        else:
            print(0)
# } Driver Code Ends