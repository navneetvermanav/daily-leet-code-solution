class Solution:
    def customSortString(self, order: str, str: str) -> str:
        cnt = Counter(str)
        ans = []
        for c in order:
            if cnt[c] > 0:
                ans.append(cnt[c] * c)
                cnt.pop(c)
        for c, v in cnt.items():
            ans.append(v * c)
        return "".join(ans)