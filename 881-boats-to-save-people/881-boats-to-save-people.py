class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count=0
        i, j =0, len(people)-1
        while i <= j :
            if people[j]==limit or people[i]+people[j]>limit:
                j-=1
                count+=1
            else:
                i+=1
                j-=1
                count+=1
        return count