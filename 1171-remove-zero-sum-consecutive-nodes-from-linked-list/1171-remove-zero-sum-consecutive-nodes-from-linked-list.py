class Solution(object):
   def removeZeroSumSublists(self, head):
       repeat = True
       while repeat:
           repeat = False
           hashMap = {}
           runningSum = 0
           cur = head 
           while cur:
               runningSum += cur.val
               if runningSum == 0:
                   head = cur.next
                   repeat = True
               else:
                   if runningSum not in hashMap:
                       hashMap[runningSum] = cur 
                   else:
                       hashMap[runningSum].next = cur.next
                       repeat = True
               cur = cur.next

       return head