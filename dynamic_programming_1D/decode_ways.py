class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        memo = [0] * (len(s) + 1)
        memo[0], memo[1] = 1, 1

        for i in range(2, len(s) + 1):
            ones = int(s[i - 1])
            twos = int(s[i - 2 : i])

            if 1 <= ones <= 9:
                memo[i] += memo[i - 1]
            if 10 <= twos <= 26:
                memo[i] += memo[i - 2]

        return memo[len(s)]


test_cases = ["12", "226", "06", "11106"]
sol = Solution()
for case in test_cases:
    print(sol.numDecodings(case))
# print(sol.numDecodings(test_cases[3]))
