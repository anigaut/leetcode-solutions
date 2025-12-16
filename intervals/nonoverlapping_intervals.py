from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def is_overlapping(i1, i2):
            return i1[0] < i2[1] and i2[0] < i1[1]
        
        def merge_intervals(i1, i2):
            return [max(i1[0], i2[0]), min(i1[1], i2[1])]
        
        intervals.sort(key=lambda x: x[0])
        new = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = new[-1]
            cur = intervals[i]

            if is_overlapping(prev, cur):
                new.pop()
                new.append(merge_intervals(prev, cur))
            else:
                new.append(cur)
        
        return len(intervals) - len(new)

sol = Solution()
test_cases = [
    [[1,2],[2,3],[3,4],[1,3]],
    [[1,2],[1,2],[1,2]],
    [[1,2],[2,3]]
]

# for case in test_cases:
#     print(sol.eraseOverlapIntervals(case))

print(sol.eraseOverlapIntervals(test_cases[2]))


