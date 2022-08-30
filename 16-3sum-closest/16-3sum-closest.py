class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=sum(nums[:3])
        for i in range(len(nums)-2):
            s=i+1
            r=len(nums)-1
            while s<r:
                sumhere=nums[i]+nums[s]+nums[r]
                if abs(sumhere-target)<abs(res-target):
                    res=sumhere
                if sumhere<target:
                    s+=1
                else:
                    r-=1
        return res
                
        
        