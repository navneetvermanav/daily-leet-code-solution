class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:


        events.sort(key = lambda x: x[0])
        N = len(events)


        @cache
        def calc(index, currentDay, currentK):
            if index == N or currentK == 0:
                return 0

            while index < N and events[index][0] <= currentDay:
                index += 1
            
            if index == N:
                return 0

            best = 0

            for j in range(index, N):
                best = max(best, events[j][2] + calc(j + 1, events[j][1], currentK - 1))

            return best

        return calc(0, 0, k)