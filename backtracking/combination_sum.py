'''
- Note that that unlike the subsets problem, we can use the same number many times.
- Base cases can be tricky. Think about all instances where we either reach the target or exceed or the index moves beyond the length of candidates.
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur = [], []

        def backtrack(i, total):
            if total == target:
                res.append(cur[:])
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            backtrack(i, total + candidates[i])
            cur.pop()
            backtrack(i + 1, total)

        backtrack(0, 0)
        return res 
