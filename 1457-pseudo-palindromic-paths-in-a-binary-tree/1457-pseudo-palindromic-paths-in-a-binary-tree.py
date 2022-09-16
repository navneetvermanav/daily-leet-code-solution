class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        self.paths=0
        pathdict=defaultdict(int)
        def dfs(node):
            if not node.left and not node.right:
                pathdict[node.val]+=1
                if self.couldPalindrome(pathdict):
                    self.paths+=1
                pathdict[node.val]-=1
                return
            pathdict[node.val]+=1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            pathdict[node.val]-=1
            if not pathdict[node.val]:
                del pathdict[node.val]
                
        dfs(root)       
        return self.paths
   

    def couldPalindrome(self,pathdict):
        
        oddcount=0
        for key in pathdict:
            if pathdict[key]%2:
                oddcount+=1
                
        if oddcount>1:
            return False
        return True