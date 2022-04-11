# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = head
        trav = head
        l = 0
        while c:
            l+=1
            c = c.next
        print(l)
        l = l//2 + 1
        t = 1
        while t<l:
            trav = trav.next
            t+=1
        return trav