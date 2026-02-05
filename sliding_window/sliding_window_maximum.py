import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0
        max_heap = []

        for i in range(len(nums)):
            while max_heap and max_heap[0][1] < left:
                heapq.heappop(max_heap)
            
            heapq.heappush(max_heap, (-nums[i], i))

            if i - left == k - 1:
                res.append(-max_heap[0][0])
                left += 1
        
        return res

sol = Solution()
test_cases = [
    ([1,3,-1,-3,5,3,6,7], 3),
    ([1], 1)
]

for case in test_cases:
    print(sol.maxSlidingWindow(case[0], case[1]))
        