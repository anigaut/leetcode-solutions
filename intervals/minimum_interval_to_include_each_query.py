import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        res = [-1] * len(queries)
        size_heap = []

        i = 0
        for (ind, query) in sorted_queries:
            while i < len(intervals) and query >= intervals[i][0]:
                start, end = intervals[i]
                heapq.heappush(size_heap, (end - start + 1, end))
                i += 1

            while size_heap and size_heap[0][1] < query:
                heapq.heappop(size_heap)
            
            if size_heap:
                res[ind] = size_heap[0][0]
            
        return res

test_cases = [
    ([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]),
    ([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]),
]

sol = Solution()
for case in test_cases:
    print(sol.minInterval(case[0], case[1]))
