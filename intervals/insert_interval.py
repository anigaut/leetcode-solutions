from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def is_overlapping(i1, i2):
            return i1[0] <= i2[1] and i2[0] <= i1[1]
        
        def merge_intervals(i1, i2):
            return [min(i1[0], i2[0]), max(i1[1], i2[1])]
        
        non_overlapping = []
        merged = []
        res = []

        for interval in intervals:
            if is_overlapping(interval, newInterval):
                merged = merge_intervals(interval, newInterval)
                newInterval = merged
            else:
                non_overlapping.append(interval)
        
        if not merged:
            merged = newInterval
        
        if not non_overlapping:
            return [merged]
        
        for interval in non_overlapping:
            if merged and merged[0] < interval[0]:
                res.append(merged)
                merged = []
            res.append(interval)
        
        if merged:
            res.append(merged)
                
        return res

test_cases = [
    ([[1,3],[6,9]], [2,5]),
    ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),
    ([[1,3],[4,6]], [2,5])
]

sol = Solution()
for case in test_cases:
    print(sol.insert(case[0], case[1]))
# print(sol.insert(test_cases[2][0], test_cases[2][1]))