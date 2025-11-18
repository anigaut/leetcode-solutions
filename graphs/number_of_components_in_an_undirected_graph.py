# From neetcode
from collections import defaultdict
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        adj_list = defaultdict(list)
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        visited = set()
        visiting = set()
        def dfs(node):
            if node in visiting:
                return
            visiting.add(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            
            visited.add(node)
            visiting.remove(node)
        
        for vertex in range(n):
            if not vertex in visited:
                dfs(vertex)
                components += 1
        
        return components
        
sol = Solution()
test_cases = [
    (3, [[0,1], [0,2]]),
    (6, [[0,1], [1,2], [2,3], [4,5]])
]

for case in test_cases:
    print(sol.countComponents(case[0], case[1]))