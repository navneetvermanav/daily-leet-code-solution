class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
	# sort the given arrays and append the 0 and given height to get the boundary values
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        
		# as we have boundary values we can get the max difference btween the sorted array
        max_h, max_w = 0, 0
        for i in range(1,len(horizontalCuts)):
            max_h = max(max_h, abs(horizontalCuts[i-1] - horizontalCuts[i]))
        
        for i in range(1,len(verticalCuts)):
            max_w = max(max_w, abs(verticalCuts[i-1] - verticalCuts[i]))
            
		# so max heights * max width will give ma area required
        
        return (max_h*max_w) % (10**9 + 7)