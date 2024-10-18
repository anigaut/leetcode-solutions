# Simple problem - remember no number will be equal to its neighbors
# The key lies in accounting for the edge cases

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            return 1

        while left <= right:
            mid = (left + right) // 2
            
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                return mid + 1
            if mid == len(nums) - 1:
                return mid
            if nums[mid-1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1