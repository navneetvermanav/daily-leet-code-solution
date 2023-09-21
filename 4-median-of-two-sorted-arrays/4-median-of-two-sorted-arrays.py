class Solution:
     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        d = len(nums1)    
        if d % 2 == 0:
            d = (d/2)-1
            median = (nums1[int(d)]+nums1[int(d+1)]) / 2
            
        else:
            d = (d-1)/2
            median = nums1[int(d)]
            
        return median
        