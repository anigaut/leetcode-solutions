from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = float('inf')
        closest = 0

        for i in range(len(arr)):
            if abs(arr[i] - x) < diff:
                closest = i
                diff = abs(arr[i] - x)
        
        left = closest - 1
        right = closest + 1
        count = 1

        while count < k:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    left -= 1
                else:
                    right += 1
            
            count += 1
        
        return arr[left + 1 : right]
        
sol = Solution()
test_cases = [
    ([1,2,3,4,5], 4, 3),
    ([1,1,2,3,4,5], 4, -1)
]
for case in test_cases:
    print(sol.findClosestElements(case[0], case[1], case[2]))
            
            
