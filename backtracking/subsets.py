'''
- For each element, we can either include it in the current subset or not.
- Backtracking comes into play since if a number is added to the subset, we also need to remove it and explore the subsets that do not include it.
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, temp = [], []

        def backtrack(i):
            if i == len(nums):
                res.append(temp[:])
                return 
            
            backtrack(i + 1) # Don't include nums[i], just move on to the next index

            temp.append(nums[i]) # Include nums[i] in the current subset
            backtrack(i + 1)
            temp.pop()
        
        backtrack(0)
        return res