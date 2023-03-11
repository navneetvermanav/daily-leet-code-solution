class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        def buildBST(start: int, end: int) -> TreeNode:
            nonlocal head

            if start > end:
                return None

            mid = (start + end) // 2
            left = buildBST(start, mid - 1)
            root = TreeNode(head.val)
            head = head.next
            right = buildBST(mid + 1, end)
            root.left = left
            root.right = right
            return root

        length = getLength(head)
        return buildBST(0, length - 1)