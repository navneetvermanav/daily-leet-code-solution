class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        ans=max(abs(sx-fx),abs(sy-fy))
        return t>=ans if ans else t!=1