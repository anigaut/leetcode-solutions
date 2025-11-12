from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        max_area = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            seen.add((row, col))
            cur_area = 0
            stack = [(row, col)]

            while stack:
                cur_row, cur_col = stack.pop()
                cur_area += 1
                for (dr, dc) in directions:
                    r = dr + cur_row
                    c = dc + cur_col


                    if (
                        0 <= r < rows and
                        0 <= c < cols and
                        (r, c) not in seen and
                        grid[r][c] == 1
                    ):
                        stack.append((r, c))
                        seen.add((r, c))
            
            return cur_area

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and grid[row][col] == 1:
                    area = dfs(row, col)
                    max_area = max(max_area, area)
                   
        return max_area

grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

sol = Solution()
print(sol.maxAreaOfIsland(grid1))