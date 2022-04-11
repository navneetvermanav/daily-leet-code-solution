class Solution:
    def rotate(self, nums: List[int], k: int) :
        for i in range (k):
            last = nums.pop()
            nums.insert(0,last)
        return nums