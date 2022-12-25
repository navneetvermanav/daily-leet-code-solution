class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def bin_sch(num):
            lo = 0
            hi = len(prefix)-1
            ans = 0
            while lo <= hi:
                mid = (lo+hi)//2
                if prefix[mid] <= num:
                    ans = mid
                    lo = mid+1
                else:
                    hi = mid-1
            return ans
                    
        nums.sort()
        prefix = [0]
        ans = []
        for i in nums:
            prefix += [prefix[-1]+i]
        for q in queries:
            ans += [bin_sch(q)]
        return ans
