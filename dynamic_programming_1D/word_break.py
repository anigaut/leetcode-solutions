from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        can_start = [True] + ([False] * len(s))

        for i in range(1, len(s) + 1):
            for word in wordDict:
                start = i - len(word)
                if start >= 0 and can_start[start] and s[start : i] == word:
                    can_start[i] = True
                    break
        
        return can_start[-1]

test_cases = [
    ("leetcode", ["leet","code"]),
    ("applepenapple", ["apple","pen"]),
    ("catsandog", ["cats","dog","sand","and","cat"])
]

sol = Solution()

for case in test_cases:
    print(sol.wordBreak(case[0], case[1]))
