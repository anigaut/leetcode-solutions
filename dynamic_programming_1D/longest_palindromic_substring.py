class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        memo = [[False for _ in range(len(s))] for _ in range(len(s))]
        max_len = 1
        longest_pal = s[0]

        for i in range(len(s)):
            memo[i][i] = True
            for j in range(i):
                if s[i] == s[j]:
                    if i - j <= 2 or memo[j + 1][i - 1]:
                        memo[j][i] = True
                        if (i - j + 1) > max_len:
                            max_len = i - j + 1
                            longest_pal = s[j : i + 1]

        return longest_pal


test_cases = ["babad", "cbbd"]
sol = Solution()
for case in test_cases:
    print(sol.longestPalindrome(case))
