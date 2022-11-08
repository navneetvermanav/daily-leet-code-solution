class Solution:
    def makeGood(self, s: str) -> str:
        prev = '@'
        
        for idx, char in enumerate(s):
            
            if abs( ord(char)-ord(prev) ) == 32:
                return self.makeGood(s[:idx-1] + s[idx+1:])
            
            prev = char
        
        # all good
        return s