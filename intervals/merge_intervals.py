from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def is_overlapping(i1, i2):
            return i1[0] <= i2[1] and i2[0] <= i1[1]
        
        def merge_intervals(i1, i2):
            return [min(i1[0], i2[0]), max(i1[1], i2[1])]

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
 
        for i in range(1, len(intervals)):
            cur = intervals[i]
            
            while res and is_overlapping(cur, res[-1]):
                prev = res.pop()
                cur = merge_intervals(cur, prev)

            res.append(cur)

        return res

test_cases = [
    [[1,3],[2,6],[8,10],[15,18]],
    [[1,4],[4,5]],
    [[4,7],[1,4]],
    [[1, 4], [5, 6], [6, 7]],
    [[2,3],[4,5],[6,7],[8,9],[1,10]]
]

sol = Solution()
for case in test_cases:
    print(sol.merge(case))
# print(sol.merge(test_cases[3]))
