class Solution:
    def validPartition(self, A):
        a = True
        b = False
        c = A[0] == A[1]
        for i in range(2, len(A)):
            a, b, c = b, c, b and A[i] == A[i - 1] or a and (A[i] == A[i - 1] == A[i - 2] or A[i] == A[i - 1] + 1 == A[i - 2] + 2)
        return c
