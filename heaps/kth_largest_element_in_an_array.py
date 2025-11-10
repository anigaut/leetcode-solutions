from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-i for i in nums]
        heapq.heapify(max_heap)

        for i in range(k):
            largest = heapq.heappop(max_heap)
            if i == k - 1:
                return - largest