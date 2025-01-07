from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            for direction in directions:
                dfs(row + direction[0], col + direction[1])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count