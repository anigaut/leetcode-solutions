class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def backtrack(row, col, ind):
            if ind == len(word):
                return True
            
            if (
                row < 0 
                or row >= rows 
                or col < 0 
                or col >= cols 
                or (row, col) in path 
                or board[row][col] != word[ind]
                ):
                return False
            
            path.add((row, col))
            res = (
                backtrack(row - 1, col, ind + 1)
                or backtrack(row + 1, col, ind + 1)
                or backtrack(row, col - 1, ind + 1)
                or backtrack(row, col + 1, ind + 1)
            )

            path.remove((row, col))

            return res

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True

        return False