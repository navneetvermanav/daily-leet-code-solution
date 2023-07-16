class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        N = len(req_skills)
        NP = len(people)
        A = [0] * NP
        for i,x in enumerate(req_skills):
            for j,p in enumerate(people):
                if x in p:
                    A[j] |= (1<<i)
        T = (1<<N) - 1
        
        @cache
        def dp(i, x):
            if x == T or i == NP:
                return [[],x]
            
            c1 = dp(i+1,x)
            c2 = dp(i+1,x | A[i])
            
            if c2[1] != T:
                return c1
            
            if c1[1] != T:
                return (c2[0] + [i], c2[1])
            if len(c1[0]) <= len(c2[0]) + 1:
                return c1
            else:
                return (c2[0] + [i], c2[1])
            
        return dp(0,0)[0]