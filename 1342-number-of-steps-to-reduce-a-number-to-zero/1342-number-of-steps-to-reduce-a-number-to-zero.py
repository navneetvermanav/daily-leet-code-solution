class Solution:
    def numberOfSteps(self, num: int) -> int:
        tmp = num
        count = 0
        while(tmp > 0):
            tmp = tmp//2 if tmp%2==0 else tmp-1
            count = count + 1
        return count
