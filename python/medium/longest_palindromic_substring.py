class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            j = 0
            #odd case
            while 0 <= i - j < len(s) and 0 <= i + j < len(s) and s[i - j] == s[i + j]:
                j += 1
            if 2 * j - 1 >= len(res):
                res = s[i - j + 1 : i + j]
            
            #even case
            if i < len(s) - 1 and s[i] == s[i + 1]:
                j = 0
                while 0 <= i - j < len(s) and 0 <= i + j + 1 < len(s) and s[i - j] == s[i + j + 1]:
                    j += 1
                if 2 * j >= len(res):
                    res = s[i - j + 1 : i + j + 1]
        
        return res