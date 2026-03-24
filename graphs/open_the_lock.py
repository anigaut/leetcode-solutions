from collections import deque
from typing import List, Set


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def modified_add(num: int) -> int:
            if num == 9:
                return 0
            return num + 1
        
        def modified_subtract(num: int) -> int:
            if num == 0:
                return 9
            return num - 1
        
        def get_neighbours(combo: str) -> List[str]:
            neighbours: List[str] = []

            for i in range(len(combo)):
                neighbours.append(combo[:i] + f"{modified_add(int(combo[i]))}" + combo[i + 1:])
                neighbours.append(combo[:i] + f"{modified_subtract(int(combo[i]))}" + combo[i + 1:])
            
            return neighbours
        
        if "0000" in deadends:
            return -1
        
        queue = deque()
        queue.append(("0000", 0))
        seen: Set[str] = set(deadends)

        while queue:
            cur, level = queue.popleft()
            if cur == target:
                return level
            
            neighbours: List[str] = get_neighbours(cur)
            for neigh in neighbours:
                if neigh not in seen:
                    queue.append((neigh, level + 1))
                    seen.add(neigh)
    
        return -1

sol = Solution()
test_cases = [
    (["0201","0101","0102","1212","2002"], "0202"),
    (["8888"], "0009"),
    (["8887","8889","8878","8898","8788","8988","7888","9888"], "8888")
]
for case in test_cases:
    print(sol.openLock(case[0], case[1]))
                
            


