from collections import defaultdict
import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = [(grid[0][0], (0, 0))]
        seen = set()
        seen.add((0, 0))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while heap:
            time, (row, col) = heapq.heappop(heap)

            if row == rows - 1 and col == cols - 1:
                return time
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if nr < rows and nr >= 0 and nc < cols and nc >= 0:
                    if (nr, nc) not in seen:
                        heapq.heappush(heap, (max(time, grid[nr][nc]), (nr, nc)))
                        seen.add((nr, nc))
            

sol = Solution()

test_cases = [
    [[0,2],[1,3]],
    [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
]

for case in test_cases:
    print(sol.swimInWater(case))