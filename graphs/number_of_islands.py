from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()
        islands = 0

        def dfs(row, col):
            seen.add((row, col))
            stack = []
            stack.append((row, col))

            while stack:
                cur_row, cur_col = stack.pop()
                for (r, c) in directions:
                    if 0 <= cur_row + r < rows and 0 <= cur_col + c < cols and grid[cur_row + r][cur_col + c] == "1" and (cur_row + r, cur_col + c) not in seen:
                        stack.append((cur_row + r, cur_col + c))
                        seen.add((cur_row + r, cur_col + c))
                        
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in seen:
                    islands += 1
                    dfs(row, col)
        
        return islands

sol = Solution()
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(sol.numIslands(grid2))