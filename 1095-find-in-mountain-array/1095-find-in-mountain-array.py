import functools
import bisect

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        class getter:
            @functools.lru_cache(None)
            def __getitem__(self, k):
                return mountain_arr.get(k)
        get = getter()
        class desc_getter:
            def __getitem__(self, k):
                return get[k] > get[k + 1]
        class neg_getter:
            def __getitem__(self, k):
                return -get[k]        
        desc = desc_getter()
        max_k = bisect.bisect_left(desc, True, 1, mountain_arr.length() - 1)
        index = bisect.bisect_left(get, target, 0, max_k + 1)
        if index < max_k + 1 and get[index] == target:
            return index
        neg = neg_getter()
        index = bisect.bisect_left(neg, -target, max_k + 1, mountain_arr.length())
        if index < mountain_arr.length() and neg[index] == -target:
            return index
        else:
            return -1