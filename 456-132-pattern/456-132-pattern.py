class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Monotonic Decreasing Stack
        stack = []  # (num_j, minLeft)  // used to track `j` 
        # -> ie top elem of {decrStk} will be candidate for num_j
        
        curMin = nums[0] # min-left side val for current idx during traversal
        
        for k in nums[1:]:
            # find out proper {j}  // that stays on top of decreasing stack
            while stack and k >= stack[-1][0]: 
                stack.pop()
            
            # thus now nums[k] < nums[j], assured if j exists on stack !

            # check constraints
            if stack and k > stack[-1][1]:
                return True
            
            # add to stack
            stack.append((k, curMin))
            
            # -> now onwards k become candidate for j
            curMin = min(curMin, k) 
        
        return False