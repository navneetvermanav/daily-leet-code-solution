class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res, l,r = sum(cardPoints[:k]),sum(cardPoints[:k]),0
        for i in range(k):
            l-=cardPoints[k-i-1]
            r+=cardPoints[len(cardPoints)-i-1]
            res = max(res,l+r)
        return res