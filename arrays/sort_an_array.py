from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):

            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2

            left_half = merge_sort(arr[:mid])
            right_half = merge_sort(arr[mid:])

            i = j = 0
            merged = []
            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    merged.append(left_half[i])
                    i += 1
                else:
                    merged.append(right_half[j])
                    j += 1
            
            while i < len(left_half):
                merged.append(left_half[i])
                i += 1
            
            while j < len(right_half):
                merged.append(right_half[j])
                j += 1
            
            return merged
        
        return merge_sort(nums)

sol = Solution()
test_cases = [[5,2,3,1], [5,1,1,2,0,0]]
for case in test_cases:
    print(sol.sortArray(case))