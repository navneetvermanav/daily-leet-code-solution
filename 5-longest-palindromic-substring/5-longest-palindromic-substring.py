class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxx = 0
        maxstr = ""
        n = len(s)
        for i in range(len(s)):
            m = i
            l = m-1
            h = m+1
            curmax = 1
            while l>=0 and h<n:
                if s[l] != s[h]:
                    break
                curmax+=2
                l-=1
                h+=1
            
            if curmax > maxx:
                maxstr = s[l+1:h]
                maxx = curmax
        for i in range(len(s)-1):
            p1 = i
            p2 = i+1
            cur = 0
            curmxstr = ""
            while(p1>=0 and p2<n and s[p1]==s[p2]):
                cur += 2
                # print(cur,p1,p2)
                curmxstr = s[p1:p2+1]
                p1-=1
                p2+=1
            if cur> maxx:
                maxstr = curmxstr
                maxx = cur
                
        return maxstr