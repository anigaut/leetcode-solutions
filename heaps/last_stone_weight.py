from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-i for i in stones]
        
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = - heapq.heappop(max_heap)
            second = - heapq.heappop(max_heap)

            if first != second:
                heapq.heappush(max_heap, -(first - second))
        
        if len(max_heap) == 1:
            return - max_heap[0]
        return 0
    
sol = Solution()
print(sol.lastStoneWeight([1]))