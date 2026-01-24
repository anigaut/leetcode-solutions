import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        cheapest = float("inf")
        adj_list = defaultdict(list)

        for start, end, price in flights:
            adj_list[start].append((end, price))

        min_cost = {(src, -1): 0}
        heap = [(0, src, -1)]

        while heap:
            price, node, stops = heapq.heappop(heap)

            for next_node, next_price in adj_list[node]:
                total_price = price + next_price
                total_stops = stops + 1

                if (next_node, total_stops) not in min_cost or total_price < min_cost[
                    (next_node, total_stops)
                ]:
                    if total_stops <= k:
                        min_cost[(next_node, total_stops)] = total_price
                        heapq.heappush(heap, (total_price, next_node, total_stops))

        for dest, stops in min_cost:
            if dest == dst:
                cheapest = min(cheapest, min_cost[(dest, stops)])

        return -1 if cheapest == float("inf") else cheapest


sol = Solution()
test_cases = [
    (4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1),
    (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1),
    (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0),
    (5, [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]], 2, 1, 1),
    (5, [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]], 0, 2, 2),
]
for case in test_cases:
    print(sol.findCheapestPrice(case[0], case[1], case[2], case[3], case[4]))
