class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.lower() == word:
            return True
        elif word.upper() == word:
            return True
        elif word.capitalize() == word:
            return True
        else:
            return False
