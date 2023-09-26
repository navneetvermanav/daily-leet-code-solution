from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        counter=Counter(s) # it indicates the number of remaining letters ahead
        letters=set() # it only save letters in stack
        
        for c in s:
            if c not in letters:
                while stack and ord(stack[-1]) > ord(c) and counter[stack[-1]]!=0:
                    letters.remove(stack.pop())
                stack.append(c)
                letters.add(c)
            counter[c]-=1
        
        return "".join(stack)