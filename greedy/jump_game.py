from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            dist = reach - i
            num = nums[i]

            if num >= dist:
                reach = i
        
        return reach == 0

sol = Solution()

test_cases = [
    [2,3,1,1,4],
    [3,2,1,0,4]
]

for case in test_cases:
    print(sol.canJump(case))