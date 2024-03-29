from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        cnt = Counter(arr)     
        x = cnt.values()
        y = set(x)
        return len(x) == len(y)
