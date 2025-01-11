from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {idx: [] for idx in range(1, len(edges) + 1)}
        seen = set()

        def dfs(node, last):
            if node in seen:
                return True

            seen.add(node)

            for n in adj[node]:
                if n == last:
                    continue
                if dfs(n, node):
                    return True
            
            return False

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
            seen = set()
            
            if dfs(v1, v2):
                return [v1, v2]
            