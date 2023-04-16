class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        freq = [defaultdict(int) for _ in range(len(words[0]))]
        for word in words: 
            for i, c in enumerate(word): 
                freq[i][c] += 1
        
        @cache
        def fn(i, k): 
            """Return number of ways to form target[i:] w/ col k."""
            if i == len(target): return 1
            if k == len(words[0]): return 0 
            return freq[k][target[i]]*fn(i+1, k+1) + fn(i, k+1)
        
        return fn(0, 0) % 1_000_000_007