'''
- Doesn't exactly follow the decision-tree based approach, but is a recursive solution nonetheless.
- For each number in the input array, recursively find all permutations of the remaining numbers, and then insert the current number at every position in each permutation.
- Therefore, for each position in each permutation, need a copy of the permutation to avoid modifying the original one.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []

        for perm in perms:
            for i in range(len(perm) + 1):
                perm_copy = perm[:]
                perm_copy.insert(i, nums[0])
                res.append(perm_copy)
        
        return res