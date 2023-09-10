class Solution:
    def countOrders(self, n: int) -> int:
        ans = 1
        for i in range(2, n + 1):
            ans *= i
        pickup_pos = 1
        curr = 2 * n - pickup_pos
        while curr != 1:
            ans *= curr
            pickup_pos += 2
            curr = 2 * n - pickup_pos
        
        return ans % (10**9 + 7)