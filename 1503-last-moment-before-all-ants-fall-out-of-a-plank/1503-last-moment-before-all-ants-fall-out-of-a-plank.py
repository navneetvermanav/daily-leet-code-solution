class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(left + [n-x for x in right], default=0)