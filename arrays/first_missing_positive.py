# The solution will always be between [1, len(nums) + 1]
# Use the array itself as a hashtable with the index acting as the key

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] > len(nums) or nums[i] < 1:
                nums[i] = len(nums) + 2
            
        for i in range(len(nums)):
            current = abs(nums[i])
            if current <= len(nums) and current > 0:
                if nums[current - 1] > 0:
                    nums[current - 1] = -(nums[current - 1])

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1
            