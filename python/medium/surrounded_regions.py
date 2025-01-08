from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            queue = deque([(r, c)])
            board[r][c] = "T" 
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if (
                        0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O"
                    ):
                        board[nr][nc] = "T"
                        queue.append((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1) and board[r][c] == "O":
                    bfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X" 
                elif board[r][c] == "T":
                    board[r][c] = "O"

                

