class Solution:
    def countSubstrings(self, s: str) -> int:
        num_pals = len(s)
        memo = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            memo[i][i] = True
            for j in range(i):
                if s[i] == s[j] and (i - j <= 2 or memo[j + 1][i - 1]):
                    memo[j][i] = True
                    num_pals += 1

        return num_pals


test_cases = ["abc", "aaa", "xabax"]
sol = Solution()
for case in test_cases:
    print(sol.countSubstrings(case))
