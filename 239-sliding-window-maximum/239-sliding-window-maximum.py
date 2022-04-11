class Solution:
     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()
        
        for i in range(k):
            while(len(q)>0 and nums[q[-1]]<=nums[i]):
                q.pop()
            q.append(i)
        
        res = [nums[q[0]]]
        
        for i in range(k, len(nums)):
            while(len(q)>0 and nums[q[-1]]<=nums[i]):
                q.pop()
            q.append(i)
            
            if(q[0] <= (i-k)): q.popleft()
            res.append(nums[q[0]])
        
        return res