class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hsh = set() 
        i = 0
        while i < (len(s) - k + 1):
            hsh.add(s[i:i+k]) 
            i += 1
        return len(hsh) == 2 ** k