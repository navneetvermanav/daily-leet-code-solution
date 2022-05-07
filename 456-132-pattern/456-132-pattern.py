class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] 
        curMin = nums[0]
        
        for k in nums[1:]:
            while stack and k >= stack[-1][0]: 
                stack.pop()
            if stack and k > stack[-1][1]:
                return True
            
            stack.append((k, curMin))
            
            curMin = min(curMin, k) 
        
        return False