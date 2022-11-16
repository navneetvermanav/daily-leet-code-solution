class Solution:
    def guessNumber(self, n: int) -> int:
        beg = 1 
        end = n
        while beg <= end:
            num = (beg+end)//2
            pick = guess(num)
            if pick == 0:
                return num
            elif pick == 1:
                beg = num+1
            else:
                end = num