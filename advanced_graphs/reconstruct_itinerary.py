from collections import defaultdict
import heapq
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)

        for source, dest in tickets:
            heapq.heappush(adj_list[source], dest)
        
        journey = []

        def dfs(city):
            while adj_list[city]:
                next = heapq.heappop(adj_list[city])
                dfs(next)
            journey.append(city)
        
        dfs("JFK")
        journey.reverse()
        return journey

sol = Solution()

test_cases = [
    ([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]),
    ([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]),
    ([["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"], ["JFK","XYZ"]])
]

for case in test_cases:
    print(sol.findItinerary(case))

        
        
                            
