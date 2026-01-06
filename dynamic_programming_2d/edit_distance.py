class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        
        def dfs(i, j):
            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                memo[(i, j)] = min(1 + dfs(i + 1, j), 1 + dfs(i + 1, j + 1), 1 + dfs(i, j + 1))
            
            return memo[(i, j)]
        
        return dfs(0, 0)

test_cases = [
    ("horse", "ros"),
    ("intention", "execution")
]

sol = Solution()
for case in test_cases:
    print(sol.minDistance(case[0], case[1]))