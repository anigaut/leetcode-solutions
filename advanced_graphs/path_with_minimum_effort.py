import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        min_heap = []
        heapq.heappush(min_heap, (0, (0, 0)))
        visited.add((0, 0))
        max_distance = 0

        while min_heap:
            distance, (r, c) = heapq.heappop(min_heap)

            max_distance = max(max_distance, distance)
            if r == len(heights) - 1 and c == len(heights[0]) - 1:
                return max_distance

            visited.add((r, c))

            for (dr, dc) in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]):
                    if (nr, nc) not in visited:
                        heapq.heappush(min_heap, (abs(heights[nr][nc] - heights[r][c]), (nr, nc)))

        return max_distance


sol = Solution()
test_cases = [
    [[1, 2, 2], [3, 8, 2], [5, 3, 5]],
    [[1, 2, 3], [3, 8, 4], [5, 3, 5]],
    [
        [1, 2, 1, 1, 1],
        [1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1],
        [1, 1, 1, 2, 1],
    ],
    [[4, 3, 4, 10, 5, 5, 9, 2], [10, 8, 2, 10, 9, 7, 5, 6], [5, 8, 10, 10, 10, 7, 4, 2], [5, 1, 3, 1, 1, 3, 1, 9],
     [6, 4, 10, 6, 10, 9, 4, 6]]
]

for case in test_cases:
    print(sol.minimumEffortPath(case))
