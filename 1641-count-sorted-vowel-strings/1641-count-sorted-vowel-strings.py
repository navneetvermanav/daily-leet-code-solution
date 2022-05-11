class Solution(object):
    def countVowelStrings(self, n):
       
        charnum = [1] * 5
        for i in range(1, n):
            temp = [0] * 5
            for i, val in enumerate(charnum):
                for j in range(i, 5):
                    temp[j] += val
            charnum = temp
        return sum(charnum)