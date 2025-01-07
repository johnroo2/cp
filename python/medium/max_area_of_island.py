from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0 or (row, col) in visited:
                return 0
            
            visited.add((row, col))

            dir_sum = 1

            for direction in directions:
                dir_sum += dfs(row + direction[0], col + direction[1])

            return dir_sum

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))

        return area