from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {idx: [] for idx in range(n)}

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        seen = set()
        def dfs(start, parent):
            seen.add(start)
            for neighbor in adj[start]:
                if neighbor == parent: 
                    continue
                if neighbor in seen or dfs(neighbor, start):
                    return True
            return False

        if dfs(0, -1):
            return False
        
        if len(seen) < n:
            return False

        return len(seen) == n and len(edges) == n - 1
