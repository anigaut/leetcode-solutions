from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # unique_paths = 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[rows - 1][cols - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        directions = [(1, 0), (0, 1)]
        dp = {}

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]

            if r == rows - 1 and c == cols - 1:
                return 1

            res = 0
            for (dr, dc) in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if nr == rows - 1 and nc == cols - 1:
                        return 1
                    elif obstacleGrid[nr][nc] == 0:
                        res += dfs(nr, nc)

            dp[(r, c)] = res
            return res

        return dfs(0, 0)

sol = Solution()
test_cases = [
    [[0,0,0],[0,1,0],[0,0,0]],
    [[0,1],[0,0]]
]

for case in test_cases:
    print(sol.uniquePathsWithObstacles(case))



