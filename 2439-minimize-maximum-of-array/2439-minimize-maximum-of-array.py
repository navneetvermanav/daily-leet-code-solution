class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        
        for i in range(n):
            curr = nums[i]          #This is current sum
            l = 1                   #This is current length of values
            val = curr/l            #This shows current Average value
            
            #If the current Average value is greater than previous one, 
            #then we're sure than it can be transferred
            while stack and (stack[-1][2])<val:     
                x, y, z = stack.pop()
                curr += x           #Adding the previous prefix sum to current sum
                l += y              #Adding possible values
                val = curr/l        #New Average value
            
            stack.append([curr, l, val])    #Simply append it in stack
        
        #By the end, we'll have the stack with possible values of Averages
        return max(ceil(z) for x,y,z in stack)