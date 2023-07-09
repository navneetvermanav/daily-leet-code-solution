class Solution:
    def largestVariance(self, s: str) -> int:
        d = collections.defaultdict(list)
        for i, c in enumerate(s):                                       # for each letter, create a list of its indices
            d[c].append(i)
        ans = 0
        for x, chr1 in enumerate(string.ascii_lowercase):               # character 1
            for chr2 in string.ascii_lowercase[x+1:]:                   # character 2
                if chr1 == chr2 or chr1 not in d or chr2 not in d:
                    continue
                prefix = i = p1 = p2 = 0
                hi = hi_idx = lo = lo_idx = 0
                n1, n2 = len(d[chr1]), len(d[chr2])
                while p1 < n1 or p2 < n2:                               # two pointers
                    if p1 < n1 and p2 < n2:
                        if d[chr1][p1] < d[chr2][p2]:
                            prefix, p1 = prefix+1, p1+1                 # count prefix
                        else:
                            prefix, p2 = prefix-1, p2+1
                    elif p1 < n1:        
                        prefix, p1 = prefix+1, p1+1
                    else:
                        prefix, p2 = prefix-1, p2+1
                    if prefix > hi:                                     # update high value
                        hi, hi_idx = prefix, i
                    if prefix < lo:                                     # update low value
                        lo, lo_idx = prefix, i
                    ans = max(ans, min(prefix-lo, i-lo_idx-1))          # update ans by calculate difference, i-lo_idx-1 is to handle when only one elements are showing up
                    ans = max(ans, min(hi-prefix, i-hi_idx-1)) 
                    i += 1 
        return ans