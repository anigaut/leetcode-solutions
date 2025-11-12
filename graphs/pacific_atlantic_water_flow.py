from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, ocean):
            stack = [(r, c)]

            while stack:
                x, y = stack.pop()
                ocean.add((x, y))

                for (dr, dc) in directions:
                    nr = x + dr
                    nc = y + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if heights[x][y] <= heights[nr][nc] and (nr, nc) not in ocean:
                            stack.append((nr, nc))
        
        for n in range(cols):
            dfs(0, n, pacific)
        
        for m in range(rows):
            dfs(m, 0, pacific)
        
        for n in range(cols):
            dfs(rows - 1, n, atlantic)
        
        for m in range(rows):
            dfs(m, cols - 1, atlantic)
        
        common = []
        for cell in pacific:
            if cell in atlantic:
                common.append(cell)
        
        return common


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
heights2 = [[1]]
sol = Solution()
print(sol.pacificAtlantic(heights))



        