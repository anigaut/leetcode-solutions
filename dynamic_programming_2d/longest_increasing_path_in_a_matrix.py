from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        memo = {}
        longest_path = 1

        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            
            has_valid_neighbour = False

            for (x, y) in directions:
                nr, nc = row + x, col + y
                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc] > matrix[row][col]:
                        has_valid_neighbour = True
                        cur_path = 1 + dfs(nr, nc)
                        memo[(row, col)] = max(cur_path, memo[(row, col)]) if (row, col) in memo else cur_path

            if not has_valid_neighbour:
                memo[(row, col)] = 1

            return memo[(row, col)]
        
        for i in range(rows):
            for j in range(cols):
                longest_path = max(longest_path, dfs(i, j))
        
        return longest_path

test_cases = [
    [[9,9,4],[6,6,8],[2,1,1]],
    [[3,4,5],[3,2,6],[2,2,1]],
    [[1]]
]

sol = Solution()
for case in test_cases:
    print(sol.longestIncreasingPath(case))

                
