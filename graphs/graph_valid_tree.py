# Leetcode premium problem - solved on neetcode

from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        path = []
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        not_allowed = set()
        visited = set()
        
        def dfs(node, prev):
            if node in not_allowed:
                return False
            not_allowed.add(node)
            
            for neighbor in adj_list[node]:
                if neighbor != prev and not dfs(neighbor, node):
                    return False
            
            visited.add(node)
            path.append(node)
            return True

        if dfs(0, -1) and len(path) == n:
            return True
        return False
        

sol = Solution()

test_cases = [
    (5, [[0, 1], [0, 2], [0, 3], [1, 4]]),
    (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]),
    (4, [[0,1],[2,3]])
]

for case in test_cases:
    print(sol.validTree(case[0], case[1]))
