class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        sub_length = len(words[0])
        word_length = sub_length * len(words)
        word_bank = collections.Counter(words)
        total_length = len(s)
        
        lefts = []
        
        for idx1 in range(total_length - word_length + 1):
            
            if s[idx1 : idx1 + sub_length] in word_bank:

                temp = word_bank.copy()
                idx2 = idx1
                
                while idx2 + sub_length <= total_length and s[idx2:idx2 + sub_length] in temp and temp[s[idx2:idx2+sub_length]] > 0:

                    temp[s[idx2:idx2+sub_length]] -= 1
                    idx2 += sub_length

                
                if idx2 - idx1 == word_length:
                    lefts.append(idx1)
                    
        
        return lefts