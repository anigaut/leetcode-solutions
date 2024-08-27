'''
 - Use three-pointers instead of two - one that iterates through the array, and one each for left and right
 - All elements before the left pointers should be 0 and all numbers after the right pointer should be 2
 - Be careful about how the i pointer moves through the array
 '''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, left, right = 0, 0, len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                i += 1
                left += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
