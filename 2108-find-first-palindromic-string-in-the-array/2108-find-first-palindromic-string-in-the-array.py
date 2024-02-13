class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            i, j = 0, len(word) - 1
            while i < j:
                if word[i] != word[j]: break
                i += 1
                j -= 1
            else: return word
        return ""