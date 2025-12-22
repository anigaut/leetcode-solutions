class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for j in range(n + 1)] for i in range(m + 1)]
        memo[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                memo[i][j] += memo[i][j + 1] + memo[i + 1][j]

        return memo[0][0]


test_cases = [(3, 7), (3, 2)]
sol = Solution()
for case in test_cases:
    print(sol.uniquePaths(case[0], case[1]))
