from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        prereq_list = defaultdict(list)
        next_list = defaultdict(list)
        for combo in prerequisites:
            next_list[combo[1]].append(combo[0])
        
        visited = set()
        cur_path = set()
        
        def dfs(course):
            if course in visited:
                return True
            if course in cur_path:
                return False

            cur_path.add(course)

            for next in next_list[course]:
                if not dfs(next):
                    return False
                
            visited.add(course)
            cur_path.remove(course)
            order.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        order.reverse()
        return order


sol = Solution()

test_cases = [
    (2, [[1,0]]),
    (4, [[1,0],[2,0],[3,1],[3,2]]),
    (1, []),
    (4, [[1, 3], [2, 1], [3, 2]])
]

for case in test_cases:
    print(sol.findOrder(case[0], case[1]))