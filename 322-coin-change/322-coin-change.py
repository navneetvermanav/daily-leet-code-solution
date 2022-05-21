class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        required=[inf for _ in range(amount+1)]
        required[0]=0
        for idx in range(len(required)):
            if required[idx]!=inf:
                continue
            required[idx]=min([inf]+[required[idx-coin] for coin in coins if coin<=idx])+1
        
        return required[amount] if required[amount]!=inf else -1