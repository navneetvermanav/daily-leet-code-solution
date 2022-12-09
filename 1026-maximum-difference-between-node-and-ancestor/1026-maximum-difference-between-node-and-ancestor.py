class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return self.helper(root, root.val, root.val)
    
    def helper(self, node, high, low):
        if not node:
            return high - low
        high = max(high, node.val)
        low = min(low, node.val)
        return max(self.helper(node.left, high, low), self.helper(node.right,high,low))
