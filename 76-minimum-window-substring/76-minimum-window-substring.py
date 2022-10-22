class Solution:
      def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        counter_t = defaultdict(int)
        for ch in t:
            counter_t[ch] += 1
        cnt, left = 0, 0
        res, min_len = '', len(s) + 1
        for i, ch in enumerate(s):
            counter_t[ch] -= 1
            if counter_t[ch] >= 0: # when ch is in t
                cnt += 1
            while cnt == len(t):
                if i - left + 1 < min_len: # get the minimum substring
                    res = s[left:i + 1]
                    min_len = len(res)
                counter_t[s[left]] += 1
                if counter_t[s[left]] > 0: # when the left char of substring is in t
                    cnt -= 1
                left += 1
        return res
        