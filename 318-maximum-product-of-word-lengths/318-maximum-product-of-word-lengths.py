class Solution:
    
    def wordsStatus(self, str1, str2):
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in str1 and i in str2:
                return False
        return True
    
    def maxProduct(self, words):
        maximum = 0
        size = len(words)
        for i in range(size - 1):
            for j in range(i + 1, size):
                if self.wordsStatus(words[i], words[j]):
                    maximum = max(maximum, len(words[i]) * len(words[j]))
        return maximum