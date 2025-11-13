from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(r, c):
            stack = [(r, c)]

            while stack:
                x, y = stack.pop()

                for (dr, dc) in directions:
                    nr = x + dr
                    nc = y + dc

                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        board[nr][nc] == "O"
                    ):
                        stack.append((nr, nc))
                        board[nr][nc] = "D"
        
        for col in range(cols):
            if board[0][col] == "O":
                board[0][col] = "D"
                dfs(0, col)

            if board[rows - 1][col] == "O":
                board[rows - 1][col] = "D"
                dfs(rows - 1, col)
        
        for row in range(rows):
            if board[row][0] == "O":
                board[row][0] = "D"
                dfs(row, 0)

            if board[row][cols - 1] == "O":
                board[row][cols - 1] = "D"
                dfs(row, cols - 1)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "D":
                    board[row][col] = "O"
        
        print(board)
    
sol = Solution()
board1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board2 = [["X"]]
sol.solve(board2)