from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:   
        all_words = wordList + [beginWord]     
        adj_list = defaultdict(list)
        patterns = defaultdict(list)
        size = len(beginWord)

        for word in all_words:
            for i in range(size):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)
        
        for words in patterns.values():
            for i in range(len(words) - 1):
                for j in range(i + 1, len(words)):
                    word1, word2 = words[i], words[j]
                    adj_list[word1].append(word2)
                    adj_list[word2].append(word1)
        
        
        visited = set()
        queue = deque()
        queue.append((beginWord, 1))

        print(adj_list)
        
        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level
            
            if word in visited:
                continue

            for next in adj_list[word]:
                if next not in visited:
                    queue.append((next, level + 1))
            
            visited.add(word)
        
        return 0



sol = Solution()

test_cases = [
    ("hit", "cog", ["hot","dot","dog","lot","log","cog"]),
    ("hit", "cog", ["hot","dot","dog","lot","log"]),
    ("leet", "code", ["lest","leet","lose","code","lode","robe","lost"])
]

# for case in test_cases:
#     print(sol.ladderLength(case[0], case[1], case[2]))

print(sol.ladderLength(test_cases[2][0], test_cases[2][1], test_cases[2][2]))