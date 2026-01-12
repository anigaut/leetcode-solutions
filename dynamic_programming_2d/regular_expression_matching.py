class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            if j == len(p) - 1:
                return i == len(s) - 1
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            is_matching = False
            if i < len(s) and (s[i] == p[j] or p[j] == "."):
                is_matching = True
            
            if j + 1 < len(p) and p[j + 1] == "*":
                res = dfs(i, j + 2) or (is_matching and dfs(i + 1, j))
            elif is_matching:
                res = dfs(i + 1, j + 1)
            else:
                res = False
            
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)
