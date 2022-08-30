class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        Subset=[]
        def dfs(i):
            if i>=len(nums):
                res.append(Subset.copy())
                return
            # decision to include nums[i]
            Subset.append(nums[i])
            dfs(i+1)
            # decison is not include nums[i]
            Subset.pop()
            dfs(i+1)
        dfs(0)
        return res