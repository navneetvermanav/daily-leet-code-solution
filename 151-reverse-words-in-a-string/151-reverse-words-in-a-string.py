class Solution:
    def reverseWords(self, s: str) -> str:
        so=s.split()
        so=list(reversed(so))
        return (' '.join(so))
        