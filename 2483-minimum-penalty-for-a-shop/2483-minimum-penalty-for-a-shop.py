class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans=0
        cnt=least=customers.count('Y')
        for i ,j in enumerate(customers):
            if j=='N':
                cnt+=1

            else:
                cnt-=1

            if cnt<least:
                ans=i+1
                least=cnt

        return ans 