class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        zipped=list(map(list,zip(*A)))
        count=0
        for item in zipped:
            if item!=sorted(item):
                count+=1
        return count
