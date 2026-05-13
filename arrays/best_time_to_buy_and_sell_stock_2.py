from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        holding = False

        for i in range(len(prices) - 1):
            if not holding and prices[i] < prices[i + 1]:
                profit -= prices[i]
                holding = True
            elif holding and prices[i] > prices[i + 1]:
                profit += prices[i]
                holding = False

        if holding:
            profit += prices[len(prices) - 1]

        return profit


sol = Solution()
test_cases = [[7, 1, 5, 3, 6, 4], [1, 2, 3, 4, 5], [7, 6, 4, 3, 1]]
for case in test_cases:
    print(sol.maxProfit(case))
