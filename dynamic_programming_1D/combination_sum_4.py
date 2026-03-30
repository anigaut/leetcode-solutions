from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = {}

        def dfs(rem):
            if rem in dp:
                return dp[rem]
            if rem == 0:
                return 1
            if rem < nums[0]:
                return 0
            
            res = 0
            for num in nums:
                if rem - num < 0:
                    break
                res += dfs(rem - num)
            
            dp[rem] = res
            return res
        
        return dfs(target)

sol = Solution()
test_cases = [([1, 2, 3], 4), ([9], 3)]
for case in test_cases:
    print(sol.combinationSum4(case[0], case[1]))