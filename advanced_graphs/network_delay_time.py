from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for edge in times:
            adj_list[edge[0]].append((edge[1], edge[2]))
        
        min_times = [float("inf") for i in range(1, n + 1)]
        min_times[k - 1] = 0

        heap = []
        heapq.heappush(heap, (0, k))

        while heap:
            fastest, node = heapq.heappop(heap)

            for edge in adj_list[node]:
                neighbor, time = edge[0], edge[1]
                cur_min_time = min_times[neighbor - 1]

                if fastest + time < cur_min_time:
                    heapq.heappush(heap, (fastest + time, neighbor))
                    min_times[neighbor - 1] = fastest + time
        
        if max(min_times) == float("inf"):
            return -1
        return max(min_times)

sol = Solution()
test_cases = [
    ([[2,1,1],[2,3,1],[3,4,1]], 4, 2),
    ([[1,2,1]], 2, 1),
    ([[1,2,1]], 2, 2),
    ([[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]], 5, 5)
]

for case in test_cases:
    print(sol.networkDelayTime(case[0], case[1], case[2]))
        
