from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        res = [""]

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        for digit in digits:
            copy = []
            for d in digitToChar[digit]:
                for base in res:
                    copy.append(base + d)
            res = copy

        return res
                    