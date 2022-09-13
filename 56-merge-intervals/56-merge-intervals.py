class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        for currInterval in sorted(intervals):
            if not ans or ans[-1][1] < currInterval[0]:
                ans.append(currInterval)
            else:
                ans[-1][1] = max(ans[-1][1], currInterval[1])

        return ans