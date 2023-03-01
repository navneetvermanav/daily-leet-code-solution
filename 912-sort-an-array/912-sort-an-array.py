from functools import reduce
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l=[]
        l2=[]
        for x in nums:
            if x <0:
                l.append(x)
            else:
                l2.append(x)
        A=Solution.neg(l2)
        c=Solution.neg(l)
        d=[-x for x in c][::-1]
        return d+A
    
    def neg(nums):
        if nums==[]:return []
        nums=[abs(x) for x in nums]
        a=max(nums)
        b=len(str(a))
        for x in range(0,b):
            B=[[] for x in range(10)]
            for y in range(len(nums)):
                num=nums[y]//10**(x) % 10
                B[num].append(nums[y])
            print(B)
            nums=reduce(lambda x,y:x+y,B)
        return [int(x) for x in nums]