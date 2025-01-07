from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def get_board (x, y):
            return board[y][x]

        def in_board (x, y):
            return x >= 0 and y >= 0 and x < len(board[0]) and y < len(board)

        def find(last, path):
            if len(path) >= len(word):
                return True

            x, y = last
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
                nx, ny = x + dx, y + dy
                if in_board(nx, ny) and (nx, ny) not in path and get_board(nx, ny) == word[len(path)]:
                    path.add((nx, ny)) 
                    if find((nx, ny), path):
                        return True
                    path.remove((nx, ny))  

            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if get_board(j, i) == word[0]:
                    if find((j, i), set([(j, i)])):
                        return True
        
        return False

        
            