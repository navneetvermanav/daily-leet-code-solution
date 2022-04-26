class Solution(object):
    def threeSumClosest(self, nums, target):
	    # sort array in ascending order 
        nums.sort()
        
        # say initial sum is infinity
        closestSum = float('inf')
        
        # iterate over the array
        for i in range(len(nums)-2):
            
            # put a left pointer 1 ahead of the current index
            left = i+1
            
            # put a right pointer at the last index
            right = len(nums)-1
        
            # iterate till left pointer is lesser than the right pointer
            while left < right:
                
                # the current sum 
                currSum = nums[i] + nums[left] + nums[right]
                
                # update the closest sum value if the absolute diff between target and current sum is lesser than the                    
				# absolute diff between target and closest Sum
                if abs(target - closestSum) > abs(target - currSum):
                        closestSum = currSum  
                
                # move right pointer towards left (so the sum would be smaller - array is sorted) if the current sum is                  
				# greater than the target
                if currSum > target:
                    right -=1
                
                # move left pointer towards right  (so the sum would be bigger - array is sorted) if the current sum is 
                # lesser than the target
                elif currSum < target:
                   
                    left +=1
                
                # if current sum is equal to the target than simply return the target
                else:
                    return target
                
        # return closest sum - it would have the number that is closest to the target on the number line
        return closestSum