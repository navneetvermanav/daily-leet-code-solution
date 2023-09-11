class Solution(object):
    def groupThePeople(self, groupSizes):
        d = {}        
        for i,v in enumerate(groupSizes):
            if v in d:
                d[v].append(i)
            else:
                d[v] = [i]                
        return [ d[i][j:j+i] for i in d for j in range(0,len(d[i]),i) ]