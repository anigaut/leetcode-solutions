'''
- The fact that duplicates are not allowed means that we need to skip elements that have already been considered in the current path.
- Sort the input array so that duplicates are adjacent, and can be skipped easily.
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur = [], []
        candidates.sort()

        def backtrack(i, total):
            if total == target:
                res.append(cur[:])
                return
            if total > target or i == len(candidates):
                return
            
            cur.append(candidates[i])
            backtrack(i + 1, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            backtrack(i + 1, total)
        
        backtrack(0, 0)
        return res