import heapq
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)
        res = 1
        ending_heap = []
        heapq.heappush(ending_heap, intervals[0].end)

        for i in range(1, len(intervals)):
            cur = intervals[i]
            earliest_ending = heapq.heappop(ending_heap)

            if cur.start < earliest_ending:
                res += 1
                heapq.heappush(ending_heap, earliest_ending)
            heapq.heappush(ending_heap, cur.end)

        return res
