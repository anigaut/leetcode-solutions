import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        order = []
        pqueue = []
        for i in range(len(tasks)):
            task = tasks[i]
            heapq.heappush(pqueue, (task[0], (task[1], i)))
        cur_time = pqueue[0][0]
        available_tasks = []

        while len(order) < len(tasks):
            while pqueue and pqueue[0][0] <= cur_time:
                _, (duration, ind) = heapq.heappop(pqueue)
                heapq.heappush(available_tasks, (duration, ind))
            
            if available_tasks:
                cur_task_duration, cur_task_index = heapq.heappop(available_tasks)
                order.append(cur_task_index)
                cur_time += cur_task_duration
            else:
                cur_time = pqueue[0][0]
        
        return order

sol = Solution()
test_cases = [[[1,2],[2,4],[3,2],[4,1]], [[7,10],[7,12],[7,5],[7,4],[7,2]]]
for case in test_cases:
    print(sol.getOrder(case))
        
