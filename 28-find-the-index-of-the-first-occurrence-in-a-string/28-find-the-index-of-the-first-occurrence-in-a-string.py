class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for p1 in range(len(haystack)-len(needle)+1):
            if haystack[p1:p1+len(needle)] == needle:
                return p1
        return -1
                
                
          