# When the sum of the current subarray goes below 0, reset and start again from the next element

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = - float('inf')

        for num in nums:
            cur_sum += num

            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0: 
                cur_sum = 0
                
        return max_sum