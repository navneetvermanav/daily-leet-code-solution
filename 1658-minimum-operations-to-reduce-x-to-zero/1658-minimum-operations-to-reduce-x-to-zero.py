class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        pre = list(accumulate(nums, add))
        post = list(accumulate(nums[::-1], add))[::-1]
        rb = len(nums)-1
        
        def bsearch(arr, target):
            ans = bisect_left(arr, target)
            if ans<0 or ans>=len(arr):
                return -1
            return ans if arr[ans]==target else -1
        
        all_left = bsearch(pre, x)
        best = all_left+1 if all_left!=-1 else float('inf')
        
        while rb >= 0:
            curr = x - post[rb]
            if curr == 0:
                return min(best, len(nums)-rb)
            
            ans = bsearch(pre, curr)
            if ans!=-1 and rb!=ans:
                best = min(best, ans + 1 + (len(nums)-rb))
            rb -=1
                
        return best if best!=float('inf') else -1