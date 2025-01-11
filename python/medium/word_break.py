from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {0 : True}

        def helper(i):
            if i in memo:
                return memo[i]
            for word in wordDict:
                if s[i - len(word):i] == word:
                    if helper(i - len(word)):
                        memo[i] = True
                        return memo[i]
            memo[i] = False
            return memo[i]

        return helper(len(s))