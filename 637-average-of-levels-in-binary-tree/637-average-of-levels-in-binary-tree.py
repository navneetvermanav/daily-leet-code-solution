class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        ans=[]
            
        if not root:
            return 
        
        level=[]
        queue=[root]
        nextqueue=[]
            
        while queue!=[]:
            
            for root in queue:
                level.append(root.val)

                if root.left is not None:
                    nextqueue.append(root.left)

                if root.right is not None:
                    nextqueue.append(root.right)

            ans.append(sum(level) / len(level))
            
            level=[]
            queue=nextqueue
            nextqueue=[]
                
        return ans