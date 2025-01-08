from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        freshes = sum([
            1 if fruit == 1 else 0
            for row in grid
            for fruit in row
        ])

        mins = 0
        targets = []

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    targets.append((r, c)) 

        while freshes > 0:
            if not targets:
                return -1
            
            new_targets = []

            while targets:
                tr, tc = targets.pop()
                for dr, dc in directions:
                    if tr + dr >= 0 and tr + dr < ROWS and tc + dc >= 0 and tc + dc < COLS and grid[tr + dr][tc + dc] == 1:
                        grid[tr + dr][tc + dc] = 2
                        new_targets.append((tr + dr, tc + dc)) 
                        freshes -= 1

            mins += 1
            targets = new_targets

        return mins


        