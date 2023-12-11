class Solution:
    def findSpecialInteger(self, A: List[int]) -> int:
        return collections.Counter(A).most_common(1)[0][0]