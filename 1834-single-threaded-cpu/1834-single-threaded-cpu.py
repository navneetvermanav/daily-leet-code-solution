class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = deque(sorted([(enqTime, procTime, i) for i, (enqTime, procTime) in enumerate(tasks)]))
        ans = []
        q, startTime = [], tasks[0][0]
        while True:

            while tasks and tasks[0][0] <= startTime:
                enqTime, procTime, index = tasks.popleft()
                heapq.heappush(q, (procTime, index))

            if q:
                procTime, index = heapq.heappop(q)
                ans.append(index)
                startTime += procTime
            else:
                if not tasks:
                    break
                else:
                    startTime = tasks[0][0]

        return ans
