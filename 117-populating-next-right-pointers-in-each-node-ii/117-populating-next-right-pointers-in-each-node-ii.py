"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: Optional['Node']) -> Optional['Node']:
        if root is None:
            return None
        stack = [root,]
        while stack:
            
            size = len(stack)
            for i in range(size):
                Node = stack.pop(0)
                if i<size-1:
                    Node.next = stack[0]
                # else:
                #     Node.next = None
                if Node.left:
                    stack.append(Node.left)
                if Node.right:
                    stack.append(Node.right)
        return root
        