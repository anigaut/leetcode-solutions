# Leetcode premium - took from neetcode

from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def is_overlapping(i1, i2):
            return i1.start < i2.end and i2.start < i1.end
        
        intervals.sort(key=lambda interval: interval.start)

        for i in range(1, len(intervals)):
            if is_overlapping(intervals[i - 1], intervals[i]):
                return False
        
        return True