from collections import Counter
from heapq import heappush, heappop

class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        max_freq = Counter(S).most_common(1)[0][1]
        if 2*max_freq -1 > len(S):
            return ""
        else:
            heap = []
            for k,v in Counter(S).items():
                heappush(heap, (v*-1, k))
            result = []
            while heap:
                v,k = heappop(heap)
                if not result or k != result[-1]: # can add the top most element
                    result.append(k)
                    if v != -1:
                        heappush(heap,(v+1,k))
                else:                             # cannot add the top most element
                    v1,k1 = heappop(heap)
                    result.append(k1)
                    heappush(heap, (v,k))
                    if v1 != -1:
                        heappush(heap, (v1+1,k1))
            return "".join(result)