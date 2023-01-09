class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans =0
        l1 = len(num1)
        l2 = len(num2)
        
        for i in range(l1):
            m = 10**i
            for j in range(l2):
                ans+=(ord(num1[l1-1-i])-ord('0'))*(ord(num2[l2-1-j])-ord('0'))*m
                m*=10
            
        return str(ans)
