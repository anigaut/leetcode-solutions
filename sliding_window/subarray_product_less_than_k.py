class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if min(nums) >= k:
            return 0

        res = 0

        left, right = 0, 0 
        cur_prod = 1
    
        while right < len(nums):
            cur_prod *= nums[right]

            while cur_prod >= k:
                cur_prod //= nums[left]
                left += 1
            
            res += right - left + 1
            right += 1

        return res

sol = Solution()
test_cases = [([10,5,2,6], 100), ([1,2,3], 0), ([10, 2, 2, 2, 6], 100), ([10, 15, 8, 1, 2], 5)]
for case in test_cases:
    print(sol.numSubarrayProductLessThanK(case[0], case[1]))

