from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, max_sum = nums[0], nums[0]

        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)
        
        return max_sum
    
test_cases = [
    [-2,1,-3,4,-1,2,1,-5,4],
    [1],
    [5,4,-1,7,8]
]

sol = Solution()

for case in test_cases:
    print(sol.maxSubArray(case))