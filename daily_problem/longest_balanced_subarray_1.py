from collections import defaultdict
from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        def is_even(num):
            if num % 2 == 0:
                return True
            return False
        
        res = 0

        for i in range(len(nums) - 1):
            even_count = odd_count = 0
            seen = defaultdict(int)

            left = nums[i]

            if left not in seen:
                seen[left] += 1
                if is_even(left):
                    even_count += 1
                else:
                    odd_count += 1

            for j in range(i + 1, len(nums)):
                right = nums[j]

                if right not in seen:
                    seen[right] += 1
                    if is_even(right):
                        even_count += 1
                    else:
                        odd_count += 1
                
                if even_count == odd_count:
                    res = max(res, j - i + 1)
        
        return res

sol = Solution()
test_cases = [[2,5,4,3], [3,2,2,5,4], [1,2,3,2], [6, 2]]
for case in test_cases:
    print(sol.longestBalanced(case))