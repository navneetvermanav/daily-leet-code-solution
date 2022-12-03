class Solution:
    def frequencySort(self, s: str) -> str:
        return reduce(lambda a, b: a + b[1]*b[0], Counter(s).most_common(), '')