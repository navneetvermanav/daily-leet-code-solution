class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def letters(n):
            if 2 <= n <= 6:
                return [chr(ord('a') + (n - 2) * 3 + i) for i in range(3)]
            elif n == 7:
                return ['p', 'q', 'r', 's']
            elif n == 8:
                return ['t', 'u', 'v']
            elif n == 9:
                return ['w', 'x', 'y', 'z']
            
        def backtrack(i, s):
            if i >= len(digits):
                return res.append(s)
            for l in letters(int(digits[i])):
                backtrack(i + 1, s + l)
        
        if not digits: return []
        res = []
        backtrack(0, "")
        return res