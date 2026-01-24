from collections import defaultdict, deque
from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_set = defaultdict(set)

        in_degrees = {}
        for word in words:
            for letter in word:
                in_degrees[letter] = 0
                
        output = ""

        for i in range(len(words) - 1):
            prev, next = words[i], words[i + 1]
            min_len = min(len(prev), len(next))

            if prev[:min_len] == next[:min_len] and len(prev) > len(next):
                return ""
            
            for j in range(min_len):
                l1, l2 = prev[j], next[j]
                if l1 != l2:
                    if l2 not in adj_set[l1]:
                        adj_set[l1].add(l2)
                        in_degrees[l2] += 1
                    break
        
        queue = deque()

        for letter in in_degrees:
            if in_degrees[letter] == 0:
                queue.append(letter)
        
        while queue:
            cur = queue.popleft()
            output += cur

            for letter in adj_set[cur]:
                in_degrees[letter] -= 1
                if in_degrees[letter] == 0:
                    queue.append(letter)
        
        if len(output) != len(in_degrees):
            return ""
        
        return output


test_cases = [
    ["z","o"],
    ["hrn","hrf","er","enn","rfnn"],
    ["abc", "def"],
    ["abc","bcd","cde"]
]

sol = Solution()
for case in test_cases:
    print(sol.foreignDictionary(case))
            
