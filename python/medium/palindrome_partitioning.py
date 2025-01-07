from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return

            if s[j:i+1] == s[j:i+1][::-1]:
                part.append(s[j:i+1])
                dfs(i + 1, i + 1)
                part.pop()
            
            dfs(j, i + 1)
        
        dfs(0, 0)
        return res

