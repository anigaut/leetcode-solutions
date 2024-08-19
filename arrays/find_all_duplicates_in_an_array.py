'''
- Not an intuitive solution
- Use array itself as a hash table
- Use the fact that all numbers are between 1, n - when you come across a number for the first time, mark nums[number - 1] as as negative
- When you see the number for the second time, nums[number - 1] will be negative, meaning it's a duplicate.
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = []
        for i in range(len(nums)):
            cur = abs(nums[i])
            if nums[cur - 1] < 0:
                dups.append(cur)
            else:
                nums[cur - 1] = -(nums[cur - 1])
        
        return dups