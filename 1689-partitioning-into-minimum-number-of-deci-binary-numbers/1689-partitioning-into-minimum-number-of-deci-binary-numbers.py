class Solution:
    def minPartitions(self, n: str) -> int:
	
	    # First we'll initialize a variable as 0, to find the maximum digit.
        max_d = 0
		
		# Iterate in the string
        for i in n:
		
		    # We'll take the digit of present iteration.
            no = int(i)
			
			# We'll find the maximum from both the variables.
            max_d = max(max_d, no)
			
		# We'll return the max_d as it is the maximum number from the digit.
        return max_d