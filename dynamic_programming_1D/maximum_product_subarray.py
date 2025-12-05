from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        forward_prod = 1
        backward_prod = 1
        max_prod = min(nums) - 1

        for i in range(n):
            forward_prod *= nums[i]
            backward_prod *= nums[n - 1 - i]
            max_prod = max(max_prod, forward_prod, backward_prod)

            if forward_prod == 0:
                forward_prod = 1
            if backward_prod == 0:
                backward_prod = 1

        return max_prod


test_cases = [[2, 3, -2, 4], [-2, 0, -1], [-3, -1, -1], [-2]]
sol = Solution()
for case in test_cases:
    print(sol.maxProduct(case))
