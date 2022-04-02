class Solution:
    def validPalindrome(self, s: str) -> bool:
        def inner_check(s_slice: str) -> bool:
            length = len(s_slice)
            for i in range(length // 2):
                if s_slice[i] != s_slice[length - i - 1]:
                    return False
            return True
            
        length = len(s)
        for i in range(length // 2):
            if s[i] != s[length - i - 1]:
                return inner_check(s[i + 1:length - i]) or inner_check(s[i:length - i - 1])
        return True