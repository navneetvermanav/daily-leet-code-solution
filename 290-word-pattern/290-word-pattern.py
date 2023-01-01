class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        return len(set(zip(pattern,word)))==len(set(pattern))==len(set(word)) and len(pattern)==len(word)
        