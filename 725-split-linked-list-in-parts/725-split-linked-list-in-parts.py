class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        di=[None]*k
        count=0
        head=root
        while(root):
            count+=1
            root=root.next
        div=count//k
        rem=count%k
        print(div,rem)
        index=0
        while(head!=None):
            c=1
            if rem>0:
                ex=1
            else:
                ex=0
            while(c<=div+ex):
                if c==1:
                    di[index]=head
                if c==div+ex:
                    node=head
                    head=head.next
                    node.next=None
                if c!=div+ex:
                    head=head.next
                c+=1
            index+=1
            if rem:
                rem-=1
        return di
