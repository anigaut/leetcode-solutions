from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = -float("inf")
        cur_sum = 0

        for num in nums:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        
        min_sum = float("inf")
        cur_sum = 0

        for num in nums:
            cur_sum = min(num, cur_sum + num)
            min_sum = min(min_sum, cur_sum)
        
        max_circular_sum = sum(nums) - min_sum
        
        if max_sum > 0:
            return max(max_sum, max_circular_sum) # type: ignore
        
        return max_sum # type: ignore

sol = Solution()
test_cases = [[1,-2,3,-2], [5,-3,5], [-3,-2,-3]]
for case in test_cases:
    print(sol.maxSubarraySumCircular(case))
