from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combos = []
        cur_combo = []

        def backtrack(i):
            if i > n:
                return
            
            cur_combo.append(i)
            if len(cur_combo) == k:
                combos.append(cur_combo.copy())
            else:
                backtrack(i + 1)
            
            cur_combo.pop()
            backtrack(i + 1)

        backtrack(1)
        return combos


sol = Solution()
test_cases = [(4, 2), (1, 1)]
for case in test_cases:
    print(sol.combine(case[0], case[1]))
