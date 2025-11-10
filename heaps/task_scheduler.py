from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        queue = deque()
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        intervals = 0

        while queue or max_heap:
            intervals += 1

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1

                if count != 0:
                    queue.append((intervals + n, count))

            while queue and queue[0][0] == intervals:
                time, count = queue.popleft()
                heapq.heappush(max_heap, count)
            
        return intervals        