from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def strategy(houses):
            penultimate_max, prev_max = 0, 0
            for house in houses:
                cur = max(penultimate_max + house, prev_max)
                penultimate_max = prev_max
                prev_max = cur

            return prev_max

        return max(strategy(nums[1:]), strategy(nums[:-1]))


sol = Solution()
test_cases = [
    [2, 3, 2],
    [1, 2, 3, 1],
    [1, 2, 3],
    [1, 2, 1, 1],
    [200, 3, 140, 20, 10],
    [1, 3, 1, 3, 100],
]

# for case in test_cases:
#     print(sol.rob(case))
print(sol.rob(test_cases[5]))
