from collections import Counter
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        output = []
        start = 0
        counts = Counter(s)
        cur_part = set()

        for i in range(len(s)):
            counts[s[i]] -= 1
            cur_part.add(s[i])

            if counts[s[i]] == 0:
                cur_part.remove(s[i])
            
            if len(cur_part) == 0:
                output.append(i + 1 - start)
                start = i + 1
        
        return output

sol = Solution()

test_cases = ["ababcbacadefegdehijhklij", "eccbbbbdec"]
for case in test_cases:
    print(sol.partitionLabels(case))
            
        
