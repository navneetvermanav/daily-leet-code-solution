class Solution:
    def divide(self, di: int, div: int) -> int:
        r = 0
        a = abs(di)
        b = abs(div)
        while a>=b:
            a -= b
            r += 1
            t = 1
            t1 = b
            while a >= t1:
                a -= t1
                r += t
                t1 = t1+t1
                t = t+t
        
        
        if (di>0 and div>0) or (di<0 and div<0):
            if r>(2**31 - 1):
                return 2**31 - 1
            if r< (-1*(2**31)):
                return -1*(2**31)
            return r
        if r>(2**31):
            return -1*(2**31)
        if r< (-1*(2**31-1)):
            return 2**31 - 1
        return -1*r