from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = defaultdict(list)
        completed = set()
        ongoing = set()
        for course in prerequisites:
            prereq_map[course[1]].append(course[0])
        
        print(prereq_map)

        def dfs(course):
            if course in completed:
                return True
            if course in ongoing:
                return False
            
            ongoing.add(course)

            for next in prereq_map[course]:
                if not dfs(next):
                    return False
            
            ongoing.remove(course)
            completed.add(course)

            return True
    
        for course in range(numCourses):
            if not dfs(course):
                return False    
        return True

test_cases = [
    (2, [[1,0]]),
    (2, [[1,0],[0,1]]),
    (4, [[1, 3], [2, 1], [3, 2]]),
    (20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]),
    (5, [[1,4],[2,4],[3,1],[3,2]])
]

sol = Solution()

for case in test_cases:
    print(sol.canFinish(case[0], case[1]))