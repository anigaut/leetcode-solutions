from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
 
        def dfs(i, remaining):
            if remaining == 0:
                return 1
                
            if i >= len(coins):
                return 0

            if dp[i][remaining] != -1:
                return dp[i][remaining]
            
            res = dfs(i + 1, remaining)
            if remaining >= coins[i]:
                res += dfs(i, remaining - coins[i])
            
            dp[i][remaining] = res

            return res
        
        return dfs(0, amount)
    
test_cases = [
    (5, [1, 2, 5]),
    (3, [2]),
    (10, [10])
]

sol = Solution()
for case in test_cases:
    print(sol.change(case[0], case[1]))
