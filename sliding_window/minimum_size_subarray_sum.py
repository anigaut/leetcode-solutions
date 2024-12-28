'''
Standard sliding window problem - quite easy
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float("inf")
        left = 0
        cur_sum = 0
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_size = min(min_size, right - left + 1)
                cur_sum -= nums[left]
                left += 1
        if min_size == float("inf"):
            return 0
        else:
            return min_size