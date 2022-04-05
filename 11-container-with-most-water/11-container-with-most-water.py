class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        
        l=0
        h=len(height)-1
        
        while(l<h):
            ans = max(ans, (h-l)*min(height[l], height[h]))
            if(height[l]<height[h]):
                l+=1
            else:
                h-=1
        
        return ans