# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, prevMax, count):
            if root.val >= prevMax:  
                prevMax = root.val   #updating previous max value
                count+=1    #increasing count by 1
            
            if root.left:     
                count = dfs(root.left, prevMax, count)   
            if root.right:
                count = dfs(root.right, prevMax, count)
            
            return count
        return dfs(root, root.val, 0)