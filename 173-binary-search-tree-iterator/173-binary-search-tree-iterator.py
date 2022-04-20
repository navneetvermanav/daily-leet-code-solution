# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.mystack = []
        self.makeStack(root)
        self.mystack.reverse()
        return None
        

    def makeStack(self, root):
        if root == None:
            return root
        self.makeStack(root.left)
        self.mystack.append(root.val)
        self.makeStack(root.right)
        
    def next(self) -> int:
        if self.mystack == None:
            return None
        return self.mystack.pop(-1)

    def hasNext(self) -> bool:
        if self.mystack:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()