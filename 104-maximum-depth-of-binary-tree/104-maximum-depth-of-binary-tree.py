# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def parser(root, level=0):
            if not root:
                return level
            return max(parser(root.left, level+1), parser(root.right, level+1))
        return parser(root)