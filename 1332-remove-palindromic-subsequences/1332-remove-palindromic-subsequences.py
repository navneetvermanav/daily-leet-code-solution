class Solution:
    def isPalindromeString(self, s: str) -> False:                        
        middle = len(s) // 2                                              
        
        if len(s) % 2 == 0: return s[:middle] == s[middle:][::-1]          
        
        return  s[:middle] == s[middle+1:][::-1]                            
    
    
    def removePalindromeSub(self, s: str) -> int:                       
        return 1 if self.isPalindromeString(s) else 2  