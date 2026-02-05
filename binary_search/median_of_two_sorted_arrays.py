from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        merged = []

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        while i < m:
            merged.append(nums1[i])
            i += 1
        
        while j < n:
            merged.append(nums2[j])
            j += 1

        if (m + n) % 2 == 0:
            return (merged[(m + n) // 2 - 1] + merged[(m + n) // 2]) / 2
        else:
            return merged[(m + n) // 2]

sol = Solution()
test_cases = [
    ([1,3], [2]),
    ([1,2], [3,4])
]
for case in test_cases:
    print(sol.findMedianSortedArrays(case[0], case[1]))
