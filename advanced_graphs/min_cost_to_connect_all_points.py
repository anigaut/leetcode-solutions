from collections import defaultdict
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        for i in range(len(points) - 1):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj_list[i].append((j, dist))
                adj_list[j].append((i, dist))
        
        print(adj_list)
        heap = [(0, 0)]
        vertices = set()
        cost = 0

        while len(vertices) < len(points):
            dist, node = heapq.heappop(heap)
            if node in vertices:
                continue
            vertices.add(node)
            cost += dist

            for neigh_node, neigh_dist in adj_list[node]:
                heapq.heappush(heap, (neigh_dist, neigh_node))
        
        return cost

          
sol = Solution()
test_cases = [
    ([[0,0],[2,2],[3,10],[5,2],[7,0]]),
    ([[3,12],[-2,5],[-4,1]]),
    ([[2,-3],[-17,-8],[13,8],[-17,-15]]),
    ([[0,0],[1,1],[1,0],[-1,1]])
]
for case in test_cases:
    print(sol.minCostConnectPoints(case))