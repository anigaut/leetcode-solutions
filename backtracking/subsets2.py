'''
- Same as subsets 1 except that duplicate subsets are not allowed.
- Therefore, sort the input array so that duplicates are adjacent, and can be skipped easily.
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, cur = [], []

        def backtrack(i):
            if i == len(nums):
                res.append(cur[:])
                return
            
            cur.append(nums[i])
            backtrack(i + 1)
            cur.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        
        backtrack(0)
        return res