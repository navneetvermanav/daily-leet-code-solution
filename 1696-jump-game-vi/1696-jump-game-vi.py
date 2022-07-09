class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap = [(-nums[0],0)] 
        for i in range(1,len(nums)):
            while(heap[0][1] < i-k):
                heappop(heap)
            maxSoFar = heap[0][0]
            heappush(heap,(maxSoFar-nums[i],i))
            if(i == len(nums)-1):
                return -(maxSoFar-nums[i])
        return nums[0]