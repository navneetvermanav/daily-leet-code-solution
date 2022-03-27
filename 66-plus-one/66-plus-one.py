class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(i) for i in digits]
        number = int(''.join(digits)) + 1 
        return [int(i) for i in str(number)]