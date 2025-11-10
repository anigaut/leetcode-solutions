from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        def distance(p):
            return p[0]**2 + p[1]**2
        
        priority_queue = []
        for point in points:
            dist = distance(point)
            heapq.heappush(priority_queue, (dist, point))
        
        for i in range(k):
            res.append(heapq.heappop(priority_queue)[1])
        
        return res

sol = Solution()
points = [[1,3],[-2,2]]
k = 1

print(sol.kClosest(points, k))
