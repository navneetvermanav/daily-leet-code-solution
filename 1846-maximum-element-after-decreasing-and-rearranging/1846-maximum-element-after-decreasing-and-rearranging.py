class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        prev = 0
        for a in sorted(arr):
            prev = min(prev + 1, a)
        return prev
        