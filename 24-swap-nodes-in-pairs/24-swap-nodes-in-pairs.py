# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(val=None,next=head)
        
        prev = dummy
        cur = head
        
        while cur and cur.next:
            
            prev.next, cur.next.next, cur.next, prev, cur = cur.next, cur, cur.next.next, cur, cur.next.next
        
        return dummy.next

        