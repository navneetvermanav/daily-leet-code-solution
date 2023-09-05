"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hashmap = {}
        copiedList = Node(head.val)
        hashmap[head] = copiedList
        node = copiedList
        while head.next:
            head = head.next
            node.next = Node(head.val)
            node = node.next
            hashmap[head] = node
        
        for node, copiedNode in hashmap.items():
            if node.random:
                copiedNode.random = hashmap[node.random]
        
        return copiedList