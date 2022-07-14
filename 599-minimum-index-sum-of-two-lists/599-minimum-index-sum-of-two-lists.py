from collections import defaultdict
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        counter2 = defaultdict(lambda:-1)
        for j, s in enumerate(list2):
            counter2[s] = j
        res = None
        res_idx_sum = float('inf')
        for i, s in enumerate(list1):
            if counter2[s] != -1:
                if i + counter2[s] < res_idx_sum:
                    res_idx_sum = i + counter2[s]
                    res = [s]
                elif i + counter2[s] == res_idx_sum:
                    res.append(s)
        return res