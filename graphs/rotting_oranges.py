from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_oranges = 0
        mins = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                elif grid[row][col] == 1:
                    fresh_oranges += 1
        
        while queue:
            r, c, time = queue.popleft()
            mins = max(mins, time)

            for (dr, dc) in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    queue.append((nr, nc, time + 1))
        
        return mins if fresh_oranges == 0 else -1
                    

grid1 = [[2,1,1],[1,1,0],[0,1,1]]
grid2 = [[2,1,1],[0,1,1],[1,0,1]]
grid3 = [[0, 2]]

sol = Solution()
print(sol.orangesRotting(grid1))