from collections import deque

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def bfs(node):
            if not root:
                return 0   
            
            deq = deque()
            max_zigzag_size = 0
            
            if root.left:
                deq.append((root.left, 'l', 1))
            if root.right:
                deq.append((root.right, 'r', 1))

            while deq:
                node, from_, zigzag_size = deq.popleft()
                max_zigzag_size = max(zigzag_size, max_zigzag_size) # update max len of zigzag path
                if node.left:
                    if from_ == 'l':  # if came from left
                        deq.append((node.left, "l", 1)) # set length of zigzag path to 1
                    if from_ == 'r':  # if came from right
                        deq.append((node.left, "l", zigzag_size + 1)) # increase length of zigzag path 
                if node.right:
                    if from_ == 'l':
                        deq.append((node.right, "r", zigzag_size + 1))
                    if from_ == 'r':
                        deq.append((node.right, "r", 1))
            return max_zigzag_size
			
        return bfs(root) 