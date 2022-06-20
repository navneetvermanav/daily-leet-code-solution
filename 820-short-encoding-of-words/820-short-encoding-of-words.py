class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        l = len(words)
        trie = {}
        words.sort(key = len, reverse=1)
        encoding = 0
        # build trie backwards to find all common suffixes
        for word in words:
            word = word[::-1]
            cur = trie
            suffix_in_trie = 1
            for c in word:
                if c in cur:
                    cur = cur[c]
                else:
                    cur[c] = {}
                    cur = cur[c]
                    suffix_in_trie = 0
                    
            if not suffix_in_trie:
                encoding += len(word) + 1
                
        return encoding
    