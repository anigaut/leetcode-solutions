from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # inf = 2147483647
        queue = deque()

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    queue.append((x, y, 0))
        
        while queue:
            x, y, dist = queue.popleft()

            if dist < grid[x][y]:
                grid[x][y] = dist

            for (dx, dy) in directions:
                nx, ny = x + dx, y + dy
                if nx < len(grid) and nx >= 0 and ny < len(grid[0]) and ny >= 0:
                    if grid[nx][ny] != -1 and dist + 1 < grid[nx][ny]:
                        queue.append((nx, ny, dist + 1))
        
        print(grid)

sol = Solution()
test_cases = [
    [
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]
    ],

    [
        [0,-1],
        [2147483647,2147483647]
    ]
]

for case in test_cases:
    print(sol.islandsAndTreasure(case))

        

            

