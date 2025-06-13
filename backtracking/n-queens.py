'''
- Iterate through each row and each column in each row.
- For each cell, check if placing a queen there is valid.
- Checking row validity is easy. But for columns and the diagonals, use hashsets to keep track of which columns and diagonals are already occupied by a queen.
- For the positive diagonal, (row + col) is the same for all cells in the same diagonal.
- For the negative diagonal, (row - col) is the same for all cells in the same diagonal.
- Use backtracking to try placing a queen in each cell. If its valid, add it to the board and if not, move on.
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        res = []
        cols, pos_diag, neg_diag = set(), set(), set()
        
        def backtrack(row):
            if row == n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return
            
            for col in range(n):
                if col in cols or row - col in neg_diag or row + col in pos_diag:
                    continue
                
                cols.add(col)
                neg_diag.add(row - col)
                pos_diag.add(row + col)
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                neg_diag.remove(row - col)
                pos_diag.remove(row + col)
                board[row][col] = "."
        
        backtrack(0)
        return res