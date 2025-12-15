from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        def binary_search(arr, num):
            left, right = 0, len(arr) - 1

            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == num:
                    return mid
                elif arr[mid] > num:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left
        
        for num in nums:
            if not res or num > res[-1]:
                res.append(num)
            else:
                index = binary_search(res, num)
                res[index] = num
        
        return len(res)

test_cases = [[10,9,2,5,3,7,101,18], [0,1,0,3,2,3], [7,7,7,7,7,7,7]]
sol = Solution()
for case in test_cases:
    print(sol.lengthOfLIS(case))
        
