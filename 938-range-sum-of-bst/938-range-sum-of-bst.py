class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        if not root: 
            return 0
        
        # When value is less than low, everything on it's left doesn't matter, 
        # so only return the sum from its right children
        if root.val<low: 
            return self.rangeSumBST(root.right,low,high)
        
        # Same thing for high.
        elif root.val>high: 
            return self.rangeSumBST(root.left,low,high)
        
        # The current value is in the range, so return the sum of its left, right and own value
        else:
            return root.val + self.rangeSumBST(root.right,low,high) + self.rangeSumBST(root.left,low,high)
