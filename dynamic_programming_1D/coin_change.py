from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        inf = amount + 1

        def memoize(remaining):
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]

            res = inf

            for coin in coins:
                if remaining >= coin:
                    res = min(res, 1 + memoize(remaining - coin))

            memo[remaining] = res
            return res

        return -1 if memoize(amount) >= inf else memoize(amount)


test_cases = [([1, 2, 5], 11), ([2], 3), ([1], 0)]
sol = Solution()
for case in test_cases:
    print(sol.coinChange(case[0], case[1]))
