class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # current position, counter of overlap
        current, overlap = -math.inf, 0

        for start, end in sorted(intervals, key=lambda seg: seg[1]):

            if start >= current: 
                current = end
                
            else: 
                overlap += 1

        return overlap