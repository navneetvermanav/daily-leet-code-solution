class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix_sum = [0]
        for t in travel:
            prefix_sum.append(prefix_sum[-1] + t)
        truck_to_time = {}
        for i, g in enumerate(garbage):
            for c in g:
                truck_to_time[c] = prefix_sum[i]
        return sum(truck_to_time.values()) + sum(map(len, garbage))
        