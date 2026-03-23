from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end_of_word = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)
            cur = trie.root

            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.is_end_of_word:
                    res = min(res, dfs(j + 1))

            dp[i] = res
            return res

        return dfs(0)


sol = Solution()
test_cases = [
    ("leetscode", ["leet", "code", "leetcode"]),
    ("sayhelloworld", ["hello", "world"]),
]

for case in test_cases:
    print(sol.minExtraChar(case[0], case[1]))
