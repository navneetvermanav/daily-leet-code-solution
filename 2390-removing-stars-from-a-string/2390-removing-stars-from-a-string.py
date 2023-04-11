class Solution:
    def removeStars(self, s: str) -> str:
        outputArr = []
        for chars in s:
            if chars == '*':
                outputArr.pop()
            else:
                outputArr.append(chars)
        
        return ''.join(outputArr)