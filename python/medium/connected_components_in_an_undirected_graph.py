from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {idx:set() for idx in range(n)}

        for v1, v2 in edges:
            adj[v1].add(v2)
            adj[v2].add(v1)

        components = 0
        seen = set()

        def dfs(node):
            if node in seen:
                return

            seen.add(node)

            for n in adj[node]:
                dfs(n)

        for i in range(n):
            if i not in seen:
                components += 1
                dfs(i)
        
        return components

