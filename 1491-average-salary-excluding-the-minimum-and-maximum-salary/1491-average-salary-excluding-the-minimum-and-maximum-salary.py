class Solution:
    def average(self, salary: List[int]) -> float:
        val=0
        salary.sort()
        lent=len(salary)-2
        for i in range(1,len(salary)-1) :
            val=val+salary[i]
        return (val/lent)
            
    
            
        