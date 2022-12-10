class Solution:
    def maxProduct(self, root: TreeNode) -> int:

        def dfs(node):
            if not node: return 0

            res = node.val+dfs(node.left)+dfs(node.right)
            nodeSums.add(res)

            return res

        nodeSums = set()
        treeSum = dfs(root)
        
        n = min(nodeSums,key = lambda x: abs(x-treeSum/2))

        return n*abs(n-treeSum)%1000000007 
