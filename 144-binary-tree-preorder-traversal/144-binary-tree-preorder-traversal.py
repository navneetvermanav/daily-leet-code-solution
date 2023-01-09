class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:

                                        
        if not root: return []              
        stack, ans = [root], []            
        while stack:                        
            node = stack.pop()             
            ans.append(node.val)           
            if node.right:              
                stack.append(node.right)   
            if node. left:                  
                stack.append(node.left )    
        return ans  