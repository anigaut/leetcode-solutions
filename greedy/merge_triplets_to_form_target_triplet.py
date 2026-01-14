from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        def is_too_big(triplet, target):
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                return True
            return False
        
        merged = [0, 0, 0]

        for triplet in triplets:
            if not is_too_big(triplet, target):
                merged = [max(merged[0], triplet[0]), max(merged[1], triplet[1]), max(merged[2], triplet[2])]
        
        return merged == target

sol = Solution()

test_cases = [
    ([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]),
    ([[3,4,5],[4,5,6]], [3,2,5]),
    ([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5])
]

for case in test_cases:
    print(sol.mergeTriplets(case[0], case[1]))
