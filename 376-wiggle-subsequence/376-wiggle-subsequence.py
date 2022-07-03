class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
	    # start with a length of 1
        maxLen = 1
		# intialize with an empty state
        state = ''
        if len(nums) == 1:
            return 1
        
        for i in range(1, len(nums)):
		    # current state is 'up', since the current number is 
			# greater than the previous one
            if nums[i] > nums[i-1]:
			    # if the previous state was unknown or 'down' and 
				# currently it's going 'up', then increment the counter
				# and set the new state
                if (state == '' or state == 'down'):
                    maxLen = maxLen + 1
                state = 'up'
			# current state is 'down', since the current number is
			# lesser than the previous one
            elif nums[i] < nums[i-1]:
			    # if the previous state was unknown or up and
				# it's going down, increment the counter
				# and, set the new state
                if (state == '' or state == 'up'):
                    maxLen = maxLen + 1
                state = 'down'
                
        return maxLen