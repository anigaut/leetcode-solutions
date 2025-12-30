from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [[-1, -1] for _ in range(len(prices))]

        def memoize(day, action): 
            if day >= len(prices):
                return 0
            
            if profits[day][action] != -1:
                return profits[day][action]
            
            cooldown_profit = memoize(day + 1, action)

            if action == 0:
                buy_profit = - prices[day] + memoize(day + 1, 1)
                profits[day][0] = max(cooldown_profit, buy_profit)
            else:
                sell_profit = prices[day] + memoize(day + 2, 0)
                profits[day][1] = max(cooldown_profit, sell_profit)
            
            return profits[day][action]


        return memoize(0, 0)

test_cases = [
    [1,2,3,0,2],
    [1],
    [1,3,4,0,4]
]

sol = Solution()

for case in test_cases:
    print(sol.maxProfit(case))
