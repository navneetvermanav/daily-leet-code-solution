# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, result = self.diameter(root)
        return result -1
    
    def diameter(self, root):
        if root is None:
            return 0, 0
        left = self.diameter(root.left)
        right = self.diameter(root.right)
        
        longestPathThisNode = left[0] + right[0] + 1
        longestPathThisSubtree = max(left[1], right[1])
        longestPathThisSubtree = max(longestPathThisSubtree, longestPathThisNode)
        height = 1 + max(left[0], right[0])
        return height, longestPathThisSubtree
        