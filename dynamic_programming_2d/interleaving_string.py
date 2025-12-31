class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = [[None] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            
            if memo[i][j] is not None:
                return memo[i][j]
            
            res = False
            if i < len(s1) and s1[i] == s3[i + j]:
                res = dfs(i + 1, j)
            if not res and j < len(s2) and s2[j] == s3[i + j]:
                res = dfs(i, j + 1)
            
            memo[i][j] = res
            return res
        
        return dfs(0, 0)

test_cases = [
    ("aabcc", "dbbca", "aadbbcbcac"),
    ("aabcc", "dbbca", "aadbbbaccc"),
    ("", "", "")
]

sol = Solution()
for case in test_cases:
    print(sol.isInterleave(case[0], case[1], case[2]))
