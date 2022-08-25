
class Solution:
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in  range (0,len(nums)):
            for j in range (1,len(nums)):
                if [i]==[j+1]:
                    return j+1
        '''
class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        arr.sort()
        for i in range(len(arr)-1):
            if(arr[i]==arr[i+1]):
                return arr[i]