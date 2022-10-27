class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        bit_img1 = []
        bit_img2 = [0 for _ in range(n-1)]
        ans = 0
        for i in img1:
            tmp = ''
            for j in i:
                tmp += str(j)
            bit_img1.append(int(tmp,2))
        for i in img2:
            tmp = ''
            for j in i:
                tmp += str(j)
            tmp += '0' * (n-1)
            bit_img2.append(int(tmp,2))
        for i in range(2*n-1):
            for k in range(2*n-1):
                tmp = 0
                for j in range(n):
                    if j+i < 2*n-1: 
                        tmp += bin((bit_img1[j] << k) & bit_img2[j+i]).count('1')
                ans = max(tmp,ans)
        return ans