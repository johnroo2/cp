from math import floor
from typing import List

def isValidSudoku(self, board: List[List[str]]) -> bool:
    for i in range(9):
        row = [x for x in board[i] if x != "."]
        col = [x for x in [row[i] for row in board] if x != "."]
        box = [x for x in board[3 * (i // 3)][3 * (i % 3):(3 * (i % 3) + 3)]
        + board[3 * (i // 3) + 1][3 * (i % 3):(3 * (i % 3) + 3)]
        + board[3 * (i // 3) + 2][3 * (i % 3):(3 * (i % 3) + 3)] if x != "."]
        
        if set(row) != list(row):
            return False
        if set(col) != list(col):
            return False
        if set(box) != list(box):
            return False