# Since extra space isn't allowed, the array itself can be treated as a hash table, using the indices, similar to Find Missing Positive
# Can also be solved using Floyd's Cycle Detection Algorithm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            current = abs(nums[i])
            if nums[current] < 0:
                return current
            else:
                nums[current] = -(nums[current])
