# The key lies in finding the 'pivot' element.
# Note that if the middle element is greater than the last element in the array, the minimum lies in the right half and vice versa

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                return min(res, nums[left])
            
            mid = (left + right) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return res


