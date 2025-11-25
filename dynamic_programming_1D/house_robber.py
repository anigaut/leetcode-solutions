from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cost_from_houses = {
            n - 1: nums[n - 1]
        }
        
        if n > 1:
            cost_from_houses[n - 2] = nums[n - 2]
        if n > 2:
            cost_from_houses[n - 3] = nums[n - 3] + nums[n - 1]

        def memoize(index):
            if index in cost_from_houses:
                return cost_from_houses[index]
            if n == 1:
                return nums[0]

            cur_rev = 0 if index == -2 else nums[index]
            cost_from_houses[index] = cur_rev + max(memoize(index + 2), memoize(index + 3))

            return cost_from_houses[index]

        return memoize(-2)

sol = Solution()
test_cases = [
    [1, 2, 3, 1],
    [2, 7, 9, 3, 1]
]

for case in test_cases:
    print(sol.rob(case))
