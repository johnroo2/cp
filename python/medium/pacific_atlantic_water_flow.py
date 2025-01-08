from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        def bfs(starts):
            visited = [[0] * COLS for _ in range(ROWS)]
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                visited[r][c] = 1
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS and 0 <= nc < COLS
                        and not visited[nr][nc]
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        queue.append((nr, nc))
            return visited

        pacific_starts = [(0, c) for c in range(COLS)] + [(r, 0) for r in range(ROWS)]
        atlantic_starts = [(ROWS - 1, c) for c in range(COLS)] + [(r, COLS - 1) for r in range(ROWS)]
        
        pacific_reachable = bfs(pacific_starts)
        atlantic_reachable = bfs(atlantic_starts)

        result = [
            [r, c]
            for r in range(ROWS)
            for c in range(COLS)
            if pacific_reachable[r][c] and atlantic_reachable[r][c]
        ]
        
        return result
                




