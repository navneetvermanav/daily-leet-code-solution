class Solution(object):
    def tallestBillboard(self, rods):
        @cache
        def install(diff,index):
            if index==len(rods):
                if diff==0:
                    return 0
                return -9999999999999
            ans=max(rods[index]+install(diff+rods[index],index+1),install(diff-rods[index],index+1),install(diff,index+1))
            return ans
        return install(0,0)