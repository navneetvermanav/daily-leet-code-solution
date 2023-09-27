class Solution:
    def decodeAtIndex(self, S, K):
        lens, n = [0], len(S)
        for c in S:
            if c.isdigit():
                lens.append(lens[-1]*int(c))
            else:
                lens.append(lens[-1] + 1)
                
        for i in range(n, 0, -1):
            K %= lens[i]
            if K == 0 and S[i-1].isalpha():
                return S[i-1]