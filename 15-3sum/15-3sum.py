class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = []
        nums.sort()
        ptr1 = 0
        ptr2 = 1
        ptr3 = len(nums) -1
        while ptr1<=len(nums)-3:
            ptr2 = ptr1 + 1
            ptr3 = len(nums)-1
            while ptr2 < ptr3:
                sum = nums[ptr1] + nums[ptr2] + nums[ptr3]
                if sum == 0:
                    triplets.append([nums[ptr1], nums[ptr2], nums[ptr3]])
                    temp = nums[ptr2]
                    while ptr2 < len(nums) and nums[ptr2] == temp:
                        ptr2 += 1
                    temp=nums[ptr3]
                    while ptr3 >= 0 and nums[ptr3] == temp:
                        ptr3 -= 1
                elif sum > 0:
                    ptr3 -= 1
                else:
                    ptr2 += 1
            else:
                temp = nums[ptr1]
                while ptr1 < len(nums) and nums[ptr1] == temp:
                    ptr1 += 1
        return triplets
  