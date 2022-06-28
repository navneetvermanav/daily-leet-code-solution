class Solution:
    def minDeletions(self, s: str) -> int:
        deletions = 0
        char_counts = collections.Counter(s)
        frequency_set = set()
        for char,count in char_counts.items():
            while count > 0 and count in frequency_set:
                count -= 1
                deletions += 1
            frequency_set.add(count)
        return deletions