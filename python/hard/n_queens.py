from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(layers): #layers: [col]
            if len(layers) == n:
                res.append(layers)
                return

            for i in [num for num in range(n) if num not in layers]:
                intercepted = False
                for h, layer in enumerate(layers):
                    if abs(len(layers) - h) == abs(i - layer):
                        intercepted = True
                        break
                if not intercepted:
                    dfs(layers + [i])

        dfs([])

        for arr in res:
            for i, layer in enumerate(arr):
                arr[i] = "." * layer + "Q" + (n - layer - 1) * "."

        return res
            



