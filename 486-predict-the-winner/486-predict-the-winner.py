from collections import defaultdict

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        # use dictionary as dynamic programming table, to store the score gap
        dp_table = defaultdict( int )
        
        def optimal_pick( nums: List, left: int, right: int):
            
            if left == right:
                # Only one choice remains
                return nums[left]
            
            if (left, right) in dp_table:
                # If this query has been computed before
                # directly return by dp table
                return dp_table[ (left, right) ]
            
            # Maximize and compute the score gap by recurrence relationship
			# 
			# for player 1:
			# benefit of pick left = score of left - optimal pick of player 2 in ( left+1, right )
			# benefit of pick right = score of right - optimal pick of player 2 in ( left, right-1 )
            choose_left = nums[left] - optimal_pick( nums, left+1, right )
            choose_right = nums[right] - optimal_pick( nums, left, right-1 )
            
            dp_table[ (left, right) ] = max( choose_left, choose_right)
            return dp_table[ (left, right) ] 
        
        # ------------------------------------------------------
        
        # score gap = score of player 1 - score of player 2
        # Player 1 is winner if score gap >= 0
        return optimal_pick( nums, left = 0, right = len(nums)-1 ) >= 0