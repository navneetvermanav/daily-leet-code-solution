class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ''
        num = 0
        index = 0
        while index < len(s):
            char = s[index]
            if char not in temp:
                temp += char
                index += 1
            else:
                while char in temp:
                    temp = temp[1:]
            if len(temp) > num:
                num = len(temp)
        return num