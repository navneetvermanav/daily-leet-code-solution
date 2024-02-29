# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque()
        q.append(root)
        curr = root
        isEven = True
        while q:
            size = len(q)
            prev = float('-inf') if isEven else float('inf')
            for _ in range(size):
                curr = q.popleft()
                if isEven and (curr.val % 2 == 0 or curr.val <= prev):
                    return False
                if not isEven and (curr.val % 2 == 1 or curr.val >= prev):
                    return False
                prev = curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            isEven = not isEven
        return True