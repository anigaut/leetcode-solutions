from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        num_steps = len(cost)
        cost_from_steps_away = {1: cost[num_steps - 1], 2: cost[num_steps - 2]}

        def memoize(steps_away):
            if steps_away in cost_from_steps_away:
                return cost_from_steps_away[steps_away]

            cur_cost = 0 if steps_away > num_steps else cost[num_steps - steps_away]

            cost_from_steps_away[steps_away] = cur_cost + min(
                memoize(steps_away - 1), memoize(steps_away - 2)
            )

            return cost_from_steps_away[steps_away]

        return memoize(num_steps + 1)


test_cases = [[10, 15, 20], [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]]

sol = Solution()

for case in test_cases:
    print(sol.minCostClimbingStairs(case))
