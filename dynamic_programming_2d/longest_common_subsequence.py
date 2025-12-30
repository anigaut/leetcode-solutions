class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        def memoize(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]
                
            if text1[i] == text2[j]:
                memo[i][j] = 1 + memoize(i + 1, j + 1)
            else:
                memo[i][j] = max(memoize(i + 1, j), memoize(i, j + 1))
            
            return memo[i][j]
        
        return memoize(0, 0)


test_cases = [
    ("abcde", "ace"),
    ("abc", "abc"),
    ("abc", "def")
]

sol = Solution()
for case in test_cases:
    print(sol.longestCommonSubsequence(case[0], case[1]))