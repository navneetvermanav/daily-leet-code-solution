class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 1 and not lists[0]:
            return None

        def merge(left, right):
            if not left or not right:
                return left or right
            curr = dummy = ListNode("*")
            p1 = left
            p2 = right
            while (p1 and p2):
                if p1.val <= p2.val:
                    curr.next = p1
                    p1 = p1.next
                else:
                    curr.next = p2
                    p2 = p2.next
                curr = curr.next
            if (p1 or p2):
                curr.next = p1 if p1 else p2
            return dummy.next
                    
        
        right = len(lists)-1
        while(right != 0):
            left = 0
            while(left < right):
                lists[left] = merge(lists[left], lists[right])
                left += 1
                right -=1
            
            # to take care of even vs. odd length list
            right = left if left == right else left-1
        
        return lists[0]
