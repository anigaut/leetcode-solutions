from typing import List
from collections import defaultdict, deque


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_degrees = [0] * (len(edges) + 1)

        for v1, v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

            in_degrees[v1] += 1
            in_degrees[v2] += 1
        
        queue = deque()
        for i in range(1, len(edges) + 1):
            if in_degrees[i] == 1:
                queue.append(i)
        
        while queue:
            cur = queue.popleft()

            for neighbor in adj_list[cur]:
                in_degrees[cur] -= 1
                in_degrees[neighbor] -= 1

                if in_degrees[neighbor] == 1:
                    queue.append(neighbor)
        
        edges.reverse()
        for v1, v2 in edges:
            if in_degrees[v1] > 0 and in_degrees[v2] > 0:
                return [v1, v2]
        
        return []
        


sol = Solution()

test_cases = [
    [[1,2],[1,3],[2,3]],
    [[1,2],[2,3],[3,4],[1,4],[1,5]]
]

for case in test_cases:
    print(sol.findRedundantConnection(case))