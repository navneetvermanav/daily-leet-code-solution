class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        n = len(boxTypes)
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        i = ans = 0
        
        while i < n and truckSize > 0:
            if truckSize >= boxTypes[i][0]:
                ans += (boxTypes[i][0]*boxTypes[i][1])
                truckSize -= boxTypes[i][0]
                i += 1
            else:
                ans += truckSize*boxTypes[i][1]
                break
                
        return ans