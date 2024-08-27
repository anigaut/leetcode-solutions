'''
Can be counted as a sliding window problem too.
Remember that all values in the array are >= 1
'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        count = 0
        cur_prod = nums[0]

        while left < len(nums) and right < len(nums):
            if cur_prod < k:
                count += right - left + 1
                right += 1
                if right < len(nums):
                    cur_prod *= nums[right]
            else:
                cur_prod = cur_prod/nums[left]
                left += 1

        if count > 0:
            return count
        else:
            return 0
