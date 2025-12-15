from typing import List  # pyright: ignore[reportDeprecated]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:  # pyright: ignore[reportDeprecated]
        if sum(nums) % 2 == 1:
            return False
        
        half = sum(nums) // 2
        memo: set[int] = set()
        memo.add(0)

        for num in nums:
            next_memo: set[int] = set()
            for sub in memo:
                if sub + num == half:
                    return True
                next_memo.add(sub)
                next_memo.add(sub + num)
            
            memo = next_memo
        
        return False

test_cases = [[1,5,11,5], [1,2,3,5], [1, 2, 3, 5, 5]]
sol = Solution()

for case in test_cases:
    print(sol.canPartition(case))


        

        
        