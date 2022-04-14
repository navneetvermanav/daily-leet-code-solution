# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        pos = root
        while pos:
            if val > pos.val: pos = pos.right
            elif val < pos.val: pos = pos.left
            else:
                return pos
        return None
        