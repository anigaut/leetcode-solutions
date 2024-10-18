# Conduct two binary searches to find the first and last occurences of the target element

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(arr, target, side):
            left, right = 0, len(arr) - 1
            ind = -1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    ind = mid
                    if side == "left":
                        right = mid - 1
                    else:
                        left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return ind
        
        first = binary_search(nums, target, "left")
        last = binary_search(nums, target, "right")

        return [first, last]