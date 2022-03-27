class Solution:
    def myAtoi(self, s: str) -> int:
        ans, i = 0, 0
        while i < len(s) and s[i] == ' ':
            i += 1
            
        sign = +1
        if i < len(s):
            if s[i] == '-':
                sign = -1
                i += 1
            elif s[i] == '+':
                i += 1
            
        for j in range(i, len(s)):
            if s[j].isdigit():
                ans *= 10
                ans += ord(s[j]) - ord('0')
            else:
                
                break   
        
        ans *= sign
        
        return min(2**31-1, max(-2**31, ans))